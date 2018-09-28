from rest_framework import serializers
from rest_framework.authtoken.models import Token
from CinemaCore.models import Actor, Movie, Employee, MovieCrew, Client


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'  # [first_name, last_name]
        # read_only_fields = ['first_name']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'moviedb_id', 'duration', 'rating', 'release_date', 'actors',)  # 'movie_crew_amount'

        def get_movie_crew_amount(self, obj):
            amount = MovieCrew.objects.select_related('movie').filter(movie=obj).count()
            return amount


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 'deleted')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    def validate_first_name(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("The name is to short. it needs to be between 8 and 40 character")
        return value


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "name",
            "moviedb_id",
            "duration",
            "rating",
            "release_date",
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 'deleted',
                  'is_special_client']
        extra_kwargs = {
                        'password': {'write_only': True},
                        }


class ClientSerializer2(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        # so meta inheritance + writing all fields kinda solves it, you inherit all the extra stuff but still have to
        # specify the fields, but this actually isn't a lot of job so I guess it works fine?
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 'deleted',
                  'is_special_client']

#authentication with facebook