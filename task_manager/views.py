from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Task.objects.prefetch_related('tags').all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'priority',)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
