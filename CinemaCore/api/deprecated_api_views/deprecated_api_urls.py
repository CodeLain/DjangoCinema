from django.contrib import admin
from django.urls import path, include
from CinemaCore.api.deprecated_api_views.api_views import ActorList, ActorDetail, ActorsListByMovie, \
    MovieViewSet, EmployeeListCreate, ActivateUserView, UserListView, MovieList, MovieDetail, LoginView, EcuationView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('movies', MovieViewSet, base_name='movies')

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors_detail"),
    path("movies/", MovieList.as_view(), name="movie_detail"),
    path("movie/<int:pk>/", MovieDetail.as_view(), name="movie_list"),
    path("movie_actors/<int:pk>/", ActorsListByMovie.as_view(), name="movie_actors"),
    path("movie/<int:pk>/actors/", ActorsListByMovie.as_view(), name="movie_actors"),
    path("employees_list/", EmployeeListCreate.as_view(), name="employees_list"),
    path("login/", LoginView.as_view(), name="login"),
    path('activ_user/', ActivateUserView.as_view(), name='activate_user'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('sum/', EcuationView.as_view(), name='user_list'),

]

urlpatterns += router.urls
