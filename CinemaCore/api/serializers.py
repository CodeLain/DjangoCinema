from rest_framework import serializers
from CinemaCore.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Simple serializer with nothing wierd
    fields: ['id', 'name', 'moviedb_id', 'slug', 'duration', 'rating', 'release_date']
    Get all fields from model: ModelName._meta.fields
    Get a list of all the fields names from a model: [n.name for n in Movie._meta.fields]
    """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'moviedb_id', 'slug', 'duration', 'rating', 'release_date')