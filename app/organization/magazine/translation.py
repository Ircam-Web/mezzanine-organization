from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.pages.models import Page, RichText
from modeltranslation.translator import TranslationOptions
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from organization.magazine.models import Article, Topic, Brief, ArticleImage

@register(Article)
class ArticleTranslationOptions(TranslationOptions):

    fields = ('sub_title',)


@register(Brief)
class BriefTranslationOptions(TranslationOptions):

    fields = ('text_button', 'external_content', )

@register(Topic)
class TopicTranslationOptions(TranslationOptions):

    fields = ()

@register(ArticleImage)
class ArticleImageTranslationOptions(TranslationOptions):

    fields = ('description',)