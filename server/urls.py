from django.contrib import admin
from django.urls import path, include
from .swagger import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # include application urls
    path('api/auth/', include('authapp.urls')),
]
urlpatterns += swagger_urlpatterns