from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token as RestToken
from CinemaCore.models import Actor, Movie, MovieCrew, Employee
from CinemaCore.serializers import ActorSerializer, MovieSerializer, EmployeeSerializer
from django.contrib.auth import authenticate
import datetime

'''
class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer
'''


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorsListByMovie(generics.ListAPIView):
    def get_queryset(self):
        queryset = Actor.objects.filter(moviecrew__movie_id=self.kwargs["pk"])
        return queryset
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class EmployeeListCreate(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        employee = authenticate(username=username, password=password)

        if employee:
            user_token = RestToken.objects.filter(user=employee).last()
            return Response({"token": user_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
# from CinemaCore.models import Actor
# from CinemaCore.serializers import ActorSerializer
#
#
# class ActorList(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()[:20]
#         data = ActorSerializer(actors, many=True).data
#         return Response(data)
#
#
# class ActorDetail(APIView):
#     def get(self, request, pk):
#         actor = get_object_or_404(Actor, pk=pk)
#         data = ActorSerializer(actor).data
#         return Response(data)

