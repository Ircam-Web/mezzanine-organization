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

from __future__ import unicode_literals

import django.views.i18n
from django.contrib.auth.decorators import permission_required
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

from organization.core.views import *
from organization.agenda.views import *

_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = [
    url("^%s/(?P<slug>.*)/detail%s$" % (settings.EVENT_SLUG, _slash), EventDetailView.as_view(), name='event_detail'),
    url("^%s/" % settings.EVENT_SLUG, include("mezzanine_agenda.urls")),
    url("^dynamic-content-event/$",  permission_required('mezzanine_agenda.change_event')(DynamicContentEventView.as_view()), name='dynamic-content-event'),
]
