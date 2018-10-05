from rest_framework import generics
from rest_framework.views import APIView
from CinemaCore.api.serializers import FunctionSerializer, MovieSerializer, MovieRoomSerializer
from CinemaCore.models import MovieFunction, Movie, CinemaRoom


class FunctionList(generics.ListCreateAPIView):
    queryset = MovieFunction.objects.all()
    serializer_class = FunctionSerializer
    # page_size = 20


class MovieDetail(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class CinemaRoomDetail(generics.RetrieveAPIView):
    serializer_class = MovieRoomSerializer
    queryset = CinemaRoom.objects.all()