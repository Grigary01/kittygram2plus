# type: ignore
from rest_framework.pagination import PageNumberPagination


class CatsPagination(PageNumberPagination):
    """Кастомный класс пагингации"""
    page_size = 20
