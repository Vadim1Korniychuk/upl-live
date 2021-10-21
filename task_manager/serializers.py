from rest_framework import serializers
from task_manager.models import Tag, Task


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created', 'updated',)


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'priority',
            'status', 'tags', 'created', 'updated',
        )

