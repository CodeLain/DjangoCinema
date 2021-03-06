"""Cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CinemaCore import urls as cinema_urls
from CinemaCore.api import api_urls
from CinemaCore.api.deprecated_api_views import deprecated_api_urls as deprecated_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cinema_urls)),
    path('deprecated_api/', include(deprecated_api)),
    path('api/', include('CinemaCore.api.api_urls', namespace='api')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
