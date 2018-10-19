from django.urls import path

from CinemaCore.api.api_views import MovieList, ActorDetail, MovieDetailSlug, MovieDeleteSlug, MovieCreate, \
    MovieDetailPK, MoviesListFiltter, FunctionListOffset, FunctionListPageNumber, ActorMovies

app_name = 'CinemaCore'

urlpatterns = [
    # path('functions/', FunctionList.as_view(), name="functions_list"),
    # path('movie-detail/<int:pk>/', MovieDetail.as_view(), name="movie-detail"),
    path('movies/', MovieList.as_view(), name="movies_list"),
    path('movies/<int:pk>', MovieDetailPK.as_view(), name="movies_detail_pk"),
    path('movies/<slug:slug>', MovieDetailSlug.as_view(), name="movies_detail_slug"),
    path('delete_movie/<slug:slug>', MovieDeleteSlug.as_view(), name="delete_movie"),
    path('actor/<int:pk>', ActorDetail.as_view(), name="actor_detail"),
    path('create_movie/', MovieCreate.as_view(), name="create_movie"),
    path('movie_filter/', MoviesListFiltter.as_view(), name="movie_filter"),
    path('functions_list_offset/', FunctionListOffset.as_view(), name="functions_list_offset"),
    path('functions_list_pagenumber/', FunctionListPageNumber.as_view(), name="functions_list_pagenumber"),
    path('actor_movies/<int:pk>', ActorMovies.as_view(), name="functions_list_pagenumber"),
]
