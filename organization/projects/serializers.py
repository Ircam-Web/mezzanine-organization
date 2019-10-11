import imghdr
import uuid
import io
import base64
import binascii

from django.utils import six
from django.core.files.base import ContentFile

from drf_extra_fields.fields import Base64ImageField
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site
from versatileimagefield.serializers import VersatileImageFieldSerializer
from organization.core.serializers import UserPublicSerializer
from organization.projects.models import (Article, Person, Project,
                                          ProjectResidency,
                                          ProjectResidencyArticle)


class PersonPublicSerializer(serializers.ModelSerializer):
    # Instead of UserSerializer, we use a MethodField to avoid
    # making another object in response (= flatten the response payload)
    username = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "profile_image", "username")

    def get_username(self, obj):
        if not obj.user:
            return None
        return obj.user.username


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "external_id")


class ProjectResidencySerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    artist = PersonPublicSerializer()

    class Meta:
        model = ProjectResidency
        fields = ("id", "title", "project", "artist")


class ArticleSerializer(serializers.ModelSerializer):
    # Do NOT validate user because it will be set by ORM
    user = UserPublicSerializer(required=False)

    class Meta:
        model = Article
        fields = ("title", "content", "user")

    # Empty user field to avoid bad insert
    def validate_user(self, user):
        return None


class Base64VersatileImageFieldSerializer(
        Base64ImageField,
        VersatileImageFieldSerializer
):
    """
    .to_representation returns URL of different sizes from VersatileImageField
    .to_internal_value decode base64 string
    """
    pass


class ResidencyBlogPublicSerializer(serializers.ModelSerializer):
    residency = serializers.PrimaryKeyRelatedField(
        queryset=ProjectResidency.objects.all(),
        required=False
    )
    article = ArticleSerializer()
    image = Base64VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__1000x500'),
            # ('cropped', 'crop__400x400')
            # Other resize available:
            # https://django-versatileimagefield.readthedocs.io/en/latest/using_sizers_and_filters.html
        ],
        represent_in_base64=False,  # Allow to represent with VersatileImage
        required=False
    )

    class Meta:
        model = ProjectResidencyArticle
        fields = ("id", "residency", "article", "image")

    def validate_residency(self, residency):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        else:
            raise serializers.ValidationError("no user")

        if residency.artist.id != user.person.id:
            raise serializers.ValidationError(
                "the residency does not belongs to request.user"
            )

        return residency

    def create(self, validated_data):
        request = self.context['request']
        article = Article.objects.create(
            **validated_data['article'],
            site_id=get_current_site(request).id,
            user=request.user,
        )
        instance = ProjectResidencyArticle.objects.create(
            residency=validated_data.get('residency'),
            image=validated_data.get('image'),
            article=article,
        )
        return instance

    def update(self, instance, validated_data):
        raise NotImplementedError
