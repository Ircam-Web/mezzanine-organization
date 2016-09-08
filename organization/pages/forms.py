from dal import autocomplete

import dal_queryset_sequence
import dal_select2_queryset_sequence

from django import forms
from django.forms.widgets import HiddenInput
from django.forms import ModelForm
from mezzanine.core.models import Orderable
from organization.magazine.models import Article, Topic, Brief
from organization.pages.models import CustomPage
from organization.pages.models import DynamicContentHomeSlider, DynamicContentHomeBody, JobResponse


class DynamicContentHomeSliderForm(autocomplete.FutureModelForm):

    content_object = dal_queryset_sequence.fields.QuerySetSequenceModelField(
        queryset=autocomplete.QuerySetSequence(
            Article.objects.all(),
            CustomPage.objects.all(),
        ),
        required=False,
        widget=dal_select2_queryset_sequence.widgets.QuerySetSequenceSelect2('dynamic-content-home-slider'),
    )

    class Meta:
        model = DynamicContentHomeSlider
        fields = ('content_object',)


class DynamicContentHomeBodyForm(autocomplete.FutureModelForm):

    content_object = dal_queryset_sequence.fields.QuerySetSequenceModelField(
        queryset=autocomplete.QuerySetSequence(
            Article.objects.all(),
            CustomPage.objects.all(),
            Brief.objects.all(),
        ),
        required=False,
        widget=dal_select2_queryset_sequence.widgets.QuerySetSequenceSelect2('dynamic-content-home-body'),
    )

    class Meta:
        model = DynamicContentHomeBody
        fields = ('content_object',)


class JobResponseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobResponseForm, self).__init__(*args, **kwargs)
        self.fields['job_offer'].widget = forms.HiddenInput()

    class Meta:
        model = JobResponse
        fields = ['first_name', 'last_name', 'email', 'curriculum_vitae', 'cover_letter', 'job_offer']