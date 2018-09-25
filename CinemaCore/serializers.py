from rest_framework import serializers
from rest_framework.authtoken.models import Token
from CinemaCore.models import Actor, Movie, Employee


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' #[first_name, last_name]
        # read_only_fields = ['first_name']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


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