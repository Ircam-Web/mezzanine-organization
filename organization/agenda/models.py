from __future__ import unicode_literals
from future.builtins import str

from django.utils.translation import ugettext_lazy as _

from mezzanine_agenda.models import *
from organization.core.models import *
from organization.network.models import *


class EventBlock(Block):

    event = models.ForeignKey(Event, verbose_name=_('event'), related_name='blocks', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("block")
        verbose_name_plural = _("blocks")


class EventImage(Image):

    event = models.ForeignKey(Event, verbose_name=_('event'), related_name='images', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")


class EventDepartment(models.Model):

    event = models.ForeignKey(Event, verbose_name=_('event'), related_name='departments', blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, verbose_name=_('department'), related_name='events', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")