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
from CinemaCore.api_views.api_views import ActorList, ActorDetail, MovieDetail, MovieList, ActorsListByMovie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cinema_urls)),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors_detail"),
    path("movies/", MovieList.as_view(), name="movie_detail"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie_list"),
    path("movie_actors/<int:pk>/", ActorsListByMovie.as_view(), name="movie_actors"),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
