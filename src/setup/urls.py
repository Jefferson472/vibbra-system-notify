from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from decouple import config


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.pages.urls')),
    path('', include('apps.channels.urls')),
    path('', include('apps.email_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if config("DJANGO_TOOLBAR", cast=bool, default=False):
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
