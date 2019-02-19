# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2017 Ircam
# Copyright (c) 2016-2017 Guillaume Pellerin
# Copyright (c) 2016-2017 Emilie Zawadzki

# This file is part of mezzanine-organization.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from collections import OrderedDict
from re import match
from urllib.parse import urlparse
from django.shortcuts import render
from django.utils import timezone
#from django.views.generic import *
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.contenttypes.models import ContentType
from django.views.generic.base import *
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from dal import autocomplete
from dal_select2_queryset_sequence.views import Select2QuerySetSequenceView
from mezzanine_agenda.models import Event
from mezzanine.utils.views import paginate
from mezzanine.conf import settings
from organization.magazine.models import *
from organization.network.models import DepartmentPage, Person
from organization.pages.models import CustomPage, DynamicContentPage
from organization.core.views import SlugMixin, autocomplete_result_formatting, DynamicContentMixin
from organization.core.utils import split_events_from_other_related_content
from django.template.defaultfilters import slugify
from itertools import chain
from django.views.generic.edit import FormView
from .forms import CategoryFilterForm


class ArticleDetailView(SlugMixin, DetailView, DynamicContentMixin):

    model = Article
    template_name='magazine/article/article_detail.html'
    context_object_name = 'article'

    def get_object(self):
        articles = self.model.objects.published(for_user=self.request.user).select_related()
        return get_object_or_404(articles, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        sorting = False

        # automatic relation : dynamic content page
        pages = DynamicContentPage.objects.filter(object_id=self.object.id).all()
        pages_related = []
        for p in pages :
            if hasattr(p, 'page'):
                pages_related.append(p.page)
        if pages_related:
            context['concrete_objects'] += pages_related
            sorting = True

        # automatic relation : dynamic content article
        articles = DynamicContentArticle.objects.filter(object_id=self.object.id).all()
        articles_related = []
        for a in articles:
            try:
                if hasattr(a, 'article'):
                    articles_related.append(a.article)
            except ObjectDoesNotExist:
                continue
        if articles_related:
            context['concrete_objects'] += articles_related
            sorting = True

        # gather all and order by creation date
        if sorting:
            context['concrete_objects'].sort(key=lambda x: x.created, reverse=True)

        # classify related content to display it in another way (cf Manifeste)
        # @Todo : use tempalte tags filter_content_model instead the method below
        # context = split_events_from_other_related_content(context, related_content)

        if self.object.department:
            first_page = self.object.department.pages.first()
            if first_page:
                context['department_weaving_css_class'] = first_page.weaving_css_class
            context['department_name'] = self.object.department.name
        return context


class BriefDetailView(SlugMixin, DetailView):

    model = Brief
    template_name='magazine/inc_brief.html'
    context_object_name = 'brief'

    def get_context_data(self, **kwargs):
        context = super(BriefDetailView, self).get_context_data(**kwargs)
        return context


class BriefListView(SlugMixin, ListView):

    model = Brief
    template_name='magazine/brief/brief_list.html'
    context_object_name = 'brief'

    def get_context_data(self, **kwargs):
        context = super(BriefListView, self).get_context_data(**kwargs)
        return context


class TopicDetailView(SlugMixin, DetailView):

    model = Topic
    template_name='magazine/topic/topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        # paginate "manually" articles because we are not in a ListView
        articles = paginate(self.object.articles.published(), self.request.GET.get("page", 1),
                          settings.ARTICLE_PER_PAGE,
                          settings.MAX_PAGING_LINKS)
        context['articles'] = articles
        return context


class ObjectAutocomplete(Select2QuerySetSequenceView):

    paginate_by = settings.DAL_MAX_RESULTS

    def get_queryset(self):

        articles = Article.objects.all()
        custompage = CustomPage.objects.all()
        events = Event.objects.all()

        if self.q:
            articles = articles.filter(title__icontains=self.q)
            custompage = custompage.filter(title__icontains=self.q)
            events = events.filter(title__icontains=self.q)

        qs = autocomplete.QuerySetSequence(articles, custompage, events )

        if self.q:
            # This would apply the filter on all the querysets
            qs = qs.filter(title__icontains=self.q)

        # This will limit each queryset so that they show an equal number
        # of results.
        qs = self.mixup_querysets(qs)

        return qs

    def get_results(self, context):
        results = autocomplete_result_formatting(self, context)
        return results


class DynamicContentArticleView(Select2QuerySetSequenceView):

    paginate_by = settings.DAL_MAX_RESULTS

    def get_queryset(self):

        articles = Article.objects.all()
        events = Event.objects.all()
        pages = CustomPage.objects.all()
        persons = Person.objects.all()

        if self.q:
            articles = articles.filter(title__icontains=self.q)
            events = events.filter(title__icontains=self.q)
            pages = pages.filter(title__icontains=self.q)
            persons = persons.filter(title__icontains=self.q)

        qs = autocomplete.QuerySetSequence(articles, events, pages, persons)

        if self.q:
            # This would apply the filter on all the querysets
            qs = qs.filter(title__icontains=self.q)

        # This will limit each queryset so that they show an equal number
        # of results.
        qs = self.mixup_querysets(qs)

        return qs

    def get_results(self, context):
        results = autocomplete_result_formatting(self, context)
        return results


class ArticleListView(SlugMixin, ListView):

    model = Article
    template_name='magazine/article/article_list.html'
    context_object_name = 'objects'
    keywords = OrderedDict()

    def get_queryset(self):
        self.qs = super(ArticleListView, self).get_queryset()
        self.qs = self.qs.filter(status=2).order_by('-created')
        playlists = Playlist.objects.published().order_by('-created').distinct()

        if 'type' in self.kwargs:
            if self.kwargs['type'] == "article":
                playlists = []

            if self.kwargs['type'] == "video" or self.kwargs['type'] == "audio":
                playlists = playlists.filter(type=self.kwargs['type'])
                self.qs = []

        self.qs = sorted(
            chain( self.qs, playlists),
            key=lambda instance: instance.created,
            reverse=True)

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['keywords'] = settings.ARTICLE_KEYWORDS
        context['objects'] = paginate(self.qs, self.request.GET.get("page", 1),
                              settings.MEDIA_PER_PAGE,
                              settings.MAX_PAGING_LINKS)
        if 'type' in self.kwargs:
            context['current_keyword'] = self.kwargs['type'];
        return context


class ArticleEventView(SlugMixin, FormView, ListView):

    model = Article
    template_name='magazine/article/article_event_list.html'
    context_object_name = 'objects'
    success_url = "."
    form_class = CategoryFilterForm
    keywords = OrderedDict()

    def form_valid(self, form):
        # Ajax
        self.request.session['categories'] = form.cleaned_data['categories']
        if self.request.is_ajax():
            context = {}
            context["concrete_objects"] = self.get_queryset()
            return render(self.request, 'core/inc/cards.html', context)
        else :
            return super(ArticleEventView, self).form_valid(form)

    def get_queryset(self):
        self.qs = super(ArticleEventView, self).get_queryset()
        self.qs = self.qs.filter(status=2).order_by('-created')
        events = Event.objects.published().order_by('-created').distinct()

        if 'categories' in self.request.session and self.request.session['categories']:
            events = events.filter(category__name=self.request.session['categories'])
            self.qs = self.qs.filter(categories__title=self.request.session['categories'])
            self.request.session.pop('categories', None)

        self.qs = sorted(
            chain( self.qs, events),
            key=lambda instance: instance.created,
            reverse=True)

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(ArticleEventView, self).get_context_data(**kwargs)
        context['objects'] = paginate(self.qs, self.request.GET.get("page", 1),
                              settings.MEDIA_PER_PAGE,
                              settings.MAX_PAGING_LINKS)
        return context

