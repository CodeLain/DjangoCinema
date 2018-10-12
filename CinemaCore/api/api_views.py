from rest_framework.generics import ListAPIView

from CinemaCore.api.serializers import MovieSerializer

from CinemaCore.models import Movie


class MovieList(ListAPIView):
    """Simple list of all movies, nothing intresting"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer