from rest_framework import generics

from CinemaCore.models import Actor, Movie, MovieCrew
from CinemaCore.serializers import ActorSerializer, MovieSerializer

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

