from django.urls import path

from CinemaCore.api.api_views import MovieList


urlpatterns = [
    # path('functions/', FunctionList.as_view(), name="functions_list"),
    # path('movie-detail/<int:pk>/', MovieDetail.as_view(), name="movie-detail"),
    path('movies/', MovieList.as_view(), name="movies_list"),

]
