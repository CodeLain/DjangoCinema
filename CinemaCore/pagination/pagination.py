from rest_framework import pagination


class MovieListPaginationOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    max_limit = 4
