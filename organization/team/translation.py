from modeltranslation.translator import translator, register, TranslationOptions

from organization.team.models import *


@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):

    fields = ('description',)


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):

    fields = ('sub_title', 'content',)

@register(Team)
class TeamTranslationOptions(TranslationOptions):

    fields = ('sub_title', 'content',)


@register(Person)
class PersonTranslationOptions(TranslationOptions):

    fields = ('bio',)


@register(PersonActivity)
class PersonActivityTranslationOptions(TranslationOptions):

    fields = ('description', 'content')


@register(PersonLink)
class PersonTranslationOptions(TranslationOptions):

    pass