from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .swagger import swagger_urlpatterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/auth/', include('authapp.urls')),
)

urlpatterns += swagger_urlpatterns
