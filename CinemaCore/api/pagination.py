from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class MoviePageNumberPagination(PageNumberPagination):
    page_size = 10


class MovieLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 40