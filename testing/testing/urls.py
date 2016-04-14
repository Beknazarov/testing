""" Default urlconf for testingKg """

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


admin.autodiscover()


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'', include('base.urls')),
    url(r'^accounts/', include('accounts.urls')),
    # url(r'^profiles/', include('profiles.urls', namespace='profile')),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
