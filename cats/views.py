# type: ignore
from rest_framework import viewsets, filters

from .models import Achievement, Cat, User
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .pagination import CatsPagination
from django_filters.rest_framework import DjangoFilterBackend


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permossion_classes = (OwnerOrReadOnly,)
    # Подключаем фильтры бекенда
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,)
    # Пагинация
    pagination_class = None  # Можно также настроить и CatPagination
    # Фильтровать будем по полям color и birth_year модели Cat
    filterset_fields = ('color', 'birth_year')
    #  Нахождение чего то
    search_fields = ('color',)
    # Сортируем по url
    ordering_fields = ('name', 'birth_year')
    # Сортируем на постоянной основе
    ordering = ('birth_year',)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
