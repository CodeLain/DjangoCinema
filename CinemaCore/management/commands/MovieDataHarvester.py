import json
from datetime import timedelta, datetime

import requests
from django.core.management import BaseCommand

from CinemaCore.models import Movie, Actor, MovieCrew


# def prepare_url_to_consume(api_key, result_page):
#     return 'http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key=%s&page=%s' %(api_key, result_page)
class Command(BaseCommand):
    def handle(self, *args, **options):
        # url = 'http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key=76aa5558b982395ead98b1de183705f7&page=2'
        for x in range(1, 5):
            api_url = 'http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?&api_key={}&page={}'
            api_key = '76aa5558b982395ead98b1de183705f7'

            json_movies = requests.get(api_url.format(api_key, str(x))).json()
            print(json_movies)
            actors = Actor.objects.all()
            for movie in json_movies['results']:
                inst_movie = Movie.objects.create(name=movie['title'], moviedb_id=movie["id"],
                                                  duration=timedelta(hours=2, minutes=30),
                                                  rating=movie['vote_average'],
                                                  release_date=datetime.strptime(movie['release_date'], '%Y-%m-%d'))
                # inst_movie.actors.set(actors)
                for actor in actors:
                    movie_crew = MovieCrew.objects.create(movie=inst_movie, actor=actor, was_principal_actor=True,
                                                          role_played_description='did something')
                    movie_crew.save()

                inst_movie.save()

            # name = models.CharField(max_length=40)
            # moviedb_id = models.IntegerField(editable=False, unique=True, db_index=True)
            # duration = models.DurationField()
            # rating = models.FloatField()
            # release_date = models.DateField(default=datetime.date.today)
            # actors = models.ManyToManyField('Actor', through='MovieCrew')
