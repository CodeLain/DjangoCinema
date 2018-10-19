from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from CinemaCore.api.pagination import MoviePageNumberPagination, MovieLimitOffsetPagination

from CinemaCore.api.serializers import MovieSerializer, ActorSerializer, FunctionSerializer, MovieListSerializer, \
    ActorMovieSerializer

from CinemaCore.models import Movie, Actor, MovieCrew, MovieFunction

from random import randint


class MovieList(ListAPIView):
    """Simple list of all movies, nothing intresting"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailPK(RetrieveUpdateAPIView):
    """Simple detail of movie, nothing intresting"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_field = 'pk'


class MovieDetailSlug(RetrieveUpdateAPIView):
    """Simple detail of movie, nothing intresting"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class MovieCreate(CreateAPIView):
    """Create Movie API.
    Last movie ID is taken and increased to add to the new movie.
    Also created MovieCrews for all the actors in the app and this particular movie """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        last_movie_id = Movie.objects.values('moviedb_id').last().get('moviedb_id')
        new_movie_db_id = last_movie_id + 1
        new_movie = serializer.save(
            moviedb_id=new_movie_db_id)  # If the user that created the movie is need: user=self.request.user
        actors = Actor.objects.all()
        movie_crew_list = []
        for actor in actors:
            movie_crew_instance = MovieCrew(actor=actor, movie=new_movie,
                                            role_played_description="Did something, who knows what(?",
                                            was_principal_actor=True if randint(0, 1) is 1 else False)
            movie_crew_list.append(movie_crew_instance)

        MovieCrew.objects.bulk_create(movie_crew_list)


class MovieDeleteSlug(DestroyAPIView):
    """Simple delete movie, nothing intresting"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'


class ActorDetail(RetrieveAPIView):
    """Showing the details of one actor, nothing intresting"""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MoviesListFiltter(ListAPIView):
    """Simple list of all movies, nothing intresting"""
    # queryset = Movie.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'slug', 'rating']
    serializer_class = MovieListSerializer
    pagination_class = MovieLimitOffsetPagination

    def get_queryset(self):
        querylist_set = Movie.objects.all()
        query_params = self.request.GET
        print(self.request.GET)
        for key, value in query_params.items():
            # args = {key+'__icontains':value}
            # querylist_set = querylist_set.filter(**args) #solution for a single
            # "{'slug', 'id', 'release_date', 'rating', 'duration', 'name', 'moviedb_id'}"
            if key == 'slug':
                querylist_set = querylist_set.filter(slug__icontains=value)

            elif key == 'rating':
                querylist_set = querylist_set.filter(rating=value)

            elif key == 'rating__gte':
                querylist_set = querylist_set.filter(rating__gte=value)

            elif key == 'rating__lte':
                querylist_set = querylist_set.filter(rating__lte=value)

            elif key is 'q':
                querylist_set = querylist_set.filter(
                    # ['id', 'name', 'moviedb_id', 'slug', 'duration', 'rating', 'release_date']
                    Q(name__icontains=value) |
                    # Q(moviedb_id__icontains=query_params) |
                    Q(slug__icontains=value)
                )

        return querylist_set


class FunctionListOffset(ListAPIView):
    """
    List of functions with LimitOffsetPagination
    LimitOffsetPagination: The client includes both a "limit" and an "offset" query parameter.
    limit: The amount of values (Functions in this case) we want to see
    offset: If provided will give me the next N values after the offset.
    """
    queryset = MovieFunction.objects.all()
    serializer_class = FunctionSerializer
    pagination_class = LimitOffsetPagination


class FunctionListPageNumber(ListAPIView):
    """

    """
    queryset = MovieFunction.objects.all()
    serializer_class = FunctionSerializer
    pagination_class = PageNumberPagination


class ActorMovies(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorMovieSerializer
