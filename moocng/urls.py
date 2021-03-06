# Copyright 2012 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


handler403 = 'django.views.defaults.permission_denied'
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

js_info_dict = {
    'packages': ('moocng',),
}

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'moocng.views.home', name='home'),
    url(r'^', include('moocng.courses.urls')),
    url(r'^', include('moocng.peerreview.urls')),

    url(r'^enrollment/', include('moocng.enrollment.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('moocng.portal.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^api/', include('moocng.api.urls')),
    url(r'^badges/', include('moocng.badges.urls')),

    url(r'^saml2/ls/$', 'djangosaml2.views.logout_service', name='saml2_ls',
        kwargs={'next_page': settings.LOGOUT_REDIRECT_URL}),
    url(r'^saml2/', include('djangosaml2.urls')),

    url(r'^contact/', include('moocng.contact.urls')),

    url(r'^category/', include('moocng.categories.urls')),

    # JavaScript translations
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
