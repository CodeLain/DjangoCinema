from rest_framework import serializers
from rest_framework.authtoken.models import Token
from CinemaCore.models import Actor, Movie, Employee


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
            model = Employee
            fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 'deleted', 'password')
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