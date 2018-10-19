from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from CinemaCore.models import Movie, Actor, MovieFunction


class MovieSerializer(ModelSerializer):
    """Simple serializer with nothing wierd
    fields: ['id', 'name', 'moviedb_id', 'slug', 'duration', 'rating', 'release_date']
    Get all fields from model: ModelName._meta.fields
    Get a list of all the fields names from a model: [n.name for n in Movie._meta.fields]
    """

    class Meta:
        model = Movie
        fields = ('id', 'name', 'moviedb_id', 'slug', 'duration', 'rating', 'release_date')


class MovieListSerializer(ModelSerializer):
    """Nice Serializer with URL with all the details of the movie
    """
    url = HyperlinkedIdentityField(
        view_name='api:movies_detail_slug',
        lookup_field='slug'
    )

    class Meta:
        model = Movie
        fields = ('url', 'name', 'moviedb_id', 'duration', 'rating', 'release_date')


class ActorSerializer(ModelSerializer):
    """Simple serializer"""

    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name')


class FunctionSerializer(ModelSerializer):
    """Function serializer with a MethodField that shows the room id and also
    a HyperLinkedRelatedField that shows the foreign key with the slug! IT WORKS!"""
    movie = HyperlinkedRelatedField(
        view_name='api:movies_detail_slug',  # This can be changed to the movies_detail_pk to show the pk link
        read_only=True,
        lookup_field='slug'  # This needs to also be changed for the pk link
    )

    cinema_room = SerializerMethodField()

    class Meta:
        model = MovieFunction
        fields = ('movie', 'cinema_room', 'schedule')

    def get_cinema_room(self, obj):
        return obj.cinema_room.room_id


class ActorMovieSerializer(ModelSerializer):
    movies = SerializerMethodField()

    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'movies')

    def get_movies(self, obj):
        return MovieSerializer(obj.movie_set.all(), many=True).data

