import json

from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token as RestToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from CinemaCore.api_permissions.permissions import IsEmployee
from CinemaCore.models import Actor, Movie, MovieCrew, Employee, Token, Client
from CinemaCore.pagination.pagination import MovieListPaginationOffset
from CinemaCore.serializers import ActorSerializer, MovieSerializer, EmployeeSerializer, MovieCreateUpdateSerializer, \
    ClientSerializer, ClientSerializer2
from django.contrib.auth import authenticate, login
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
    page_size = 20

    def get(self, request, *args, **kwargs):
        actors_list = self.list(request, *args, **kwargs)
        actors_list.data = {
            "message": "requested actors list",
            "actors_list": actors_list.data
        }
        return actors_list

    def create(self, request, *args, **kwargs):
        """Overriding the creation"""
        print("CREATING AND DOING OTHER STUFF")
        return super(ActorList, self).create(request, *args, **kwargs)


class ActorsListByMovie(generics.ListAPIView):
    def get_queryset(self):
        queryset = Actor.objects.filter(moviecrew__movie_id=self.kwargs["pk"])
        return queryset
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsEmployee, ]


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieListPaginationOffset
    page_size = 20

    def list(self, request, *args, **kwargs):
        print("LISTING AND DOING OTHER STUFF")
        return super(MovieViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        return super(MovieViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class EmployeeListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        employee = authenticate(username=username, password=password)
        # login(request, employee)
        if employee:
            # user_token = RestToken.objects.filter(user=employee).last()
            # try:
            #     user_token = employee.auth_token
            # except RestToken.DoesNotExist:
            #     new_token = RestToken.objects.create(user=employee)
            #     user_token = new_token
            auth_token, _ = RestToken.objects.get_or_create(user=employee)
            return Response({"token": auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class ActivateUserView(APIView):
    permission_classes = ()
    # permission_classes = [IsAccountAdminOrReadOnly, IsAdminOrIsSelf]
    def post(self, request,):
        # username = request.data.get("username")
        # password = request.data.get("password")
        # employee = authenticate(username=username, password=password)
        # login(request, employee)
        # if employee:
            # user_token = RestToken.objects.filter(user=employee).last()
            # try:
            #     user_token = employee.auth_token
            # except RestToken.DoesNotExist:
            #     new_token = RestToken.objects.create(user=employee)
            #     user_token = new_token
        #     auth_token, _ = RestToken.objects.get_or_create(user=employee)
        #     return Response({"token": auth_token.key}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        token_value = request.data.get("token", None)
        if not token_value:
            return Response({"error": "Missing token"}, status=status.HTTP_400_BAD_REQUEST)

        user = Token.objects.get(value=token_value).user
        user.is_active = True
        user.save()
        try:
            user.client
        except Client.DoesNotExist:
            try:
                user = user.employee
                user_data = EmployeeSerializer(user).data

            except Employee.DoesNotExist:
                return Response({"error": "User not acceptable"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            data = {
                "message": "user activated",
                "user_data": user_data
            }

        return Response(data)


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer2
    permission_classes = [IsEmployee, ]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('username', 'email', )  # profile__profession

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Client.objects.all()
    #     query = self.request.query_params.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(first_name__icontains=query) |
    #             Q(last_name__icontains=query) |
    #             Q(username__icontains=query)
    #             # Q(email__icontains=query)
    #         )
    #     return queryset_list




# class ClientList(generics


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

