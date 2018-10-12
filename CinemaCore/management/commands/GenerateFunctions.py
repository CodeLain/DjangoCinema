import random
from datetime import timedelta, datetime

import requests
from django.core.management import BaseCommand

from CinemaCore.models import Movie, Actor, MovieCrew, CinemaRoom, MovieFunction
from django.db import IntegrityError
from django.utils import timezone


def generate_cinema_rooms():
    for x in range(10):
        try:
            room_id = 100 + x
            capacity = random.randint(9, 12)*5
            CinemaRoom.objects.create(room_id=room_id, capacity=capacity)
        except IntegrityError:
            continue


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_cinema_rooms()
        dates_control = {}
        for x in range(101):
            random_room = random.choice(CinemaRoom.objects.all())
            random_movie = random.choice(Movie.objects.all())

            if random_room not in dates_control:
                dates_control[random_room] = timezone.now()
            else:
                dates_control[random_room] = timezone.now() + timedelta(hours=2)

            date = dates_control[random_room]
            MovieFunction.objects.create(movie=random_movie, cinema_room=random_room, schedule=date)
