from django.urls import path

from CinemaCore.api.api_views import FunctionList, MovieDetail, CinemaRoomDetail

urlpatterns = [
    path('functions/', FunctionList.as_view(), name="functions_list"),
    path('movie-detail/<int:pk>/', MovieDetail.as_view(), name="movie-detail"),
    path('room-detail/<int:pk>/', CinemaRoomDetail.as_view(), name="room-detail"),
]
