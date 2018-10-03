from django.urls import path

from CinemaCore.api.api_views import FunctionList, MovieDetail

urlpatterns = [
    path('functions/', FunctionList.as_view(), name="functions_list"),
    path('movie-detail/', MovieDetail.as_view(), name="movie-detail"),
]
