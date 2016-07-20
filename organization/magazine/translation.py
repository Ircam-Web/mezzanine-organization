from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.pages.models import Page, RichText
from modeltranslation.translator import TranslationOptions
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from organization.magazine.models import Article, Brief

@register(Article)
#class ArticleTranslationOptions(TranslatedDisplayable, TranslatedRichText):
class ArticleTranslationOptions(TranslationOptions):

    fields = ('sub_title',)


@register(Brief)
class BriefTranslationOptions(TranslationOptions):

    fields = ('text_button', 'local_content')