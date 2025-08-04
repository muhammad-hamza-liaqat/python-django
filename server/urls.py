from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .swagger import swagger_urlpatterns

# Language switch URL
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Wrap admin and app URLs in i18n_patterns for language prefix support
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/auth/', include('authapp.urls')),
)

# Add swagger urls normally
urlpatterns += swagger_urlpatterns
