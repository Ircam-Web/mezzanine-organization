from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from mezzanine.core.models import RichText, Displayable, Slugged
from mezzanine.pages.models import Page
from mezzanine.blog.models import BlogPost
from orderable.models import Orderable
from organization.core.models import Named, Description
from organization.media.models import Photo


class Article(BlogPost, Photo):

    sub_title = models.CharField(_('sub title'), blank=True, max_length=1000)
    related_articles = models.ManyToManyField("self",
                                 verbose_name=_("Related articles"), blank=True)

    model_name = _('article')
    def get_absolute_url(self):
        return reverse("magazine-article-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _('article')


class Brief(Displayable, RichText, Orderable):

    text_button = models.CharField(blank=True, max_length=150, null=False, verbose_name='text button')
    local_content = models.URLField(blank=False, max_length=1000, null=False, verbose_name='local content')

    def get_absolute_url(self):
        return self.local_content

    class Meta:
        verbose_name = _('brief')
        ordering = ['sort_order']

class Topic(Page, RichText):
    """Topic for magazine menu"""

    articles = models.ManyToManyField(Article, verbose_name=_('articles'), blank=True)

    class Meta:
        verbose_name = _('topic')