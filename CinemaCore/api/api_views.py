from rest_framework import generics

from CinemaCore.api.serializers import FunctionSerializer, MovieSerializer
from CinemaCore.models import MovieFunction


class FunctionList(generics.ListCreateAPIView):
    queryset = MovieFunction.objects.all()
    serializer_class = FunctionSerializer
    # page_size = 20


class MovieDetail(generics.RetrieveAPIView):
    serializer_class = MovieSerializer