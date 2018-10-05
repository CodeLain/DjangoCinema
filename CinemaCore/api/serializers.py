from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from CinemaCore.models import MovieFunction, Movie, CinemaRoom


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class FunctionSerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True)
    # movie = MovieSerializer()
    movie = serializers.StringRelatedField()
    cinema_room = serializers.HyperlinkedRelatedField(view_name='room-detail', read_only=True)
    movie_detail_url = serializers.HyperlinkedRelatedField(view_name='movie-detail', read_only=True)

    class Meta:
        model = MovieFunction
        fields = ('movie', 'cinema_room', 'schedule', 'movie_detail_url')


class MovieRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaRoom
        fields = '__all__'
# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorSerializer(many=True)
#
#     class Meta:
#         model = Movie
#         fields = ('name', 'moviedb_id', 'duration', 'rating', 'release_date', 'actors',)  # 'movie_crew_amount'
#
#         def get_movie_crew_amount(self, obj):
#             amount = MovieCrew.objects.select_related('movie').filter(movie=obj).count()
#             return amount