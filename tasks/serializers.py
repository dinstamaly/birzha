from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from .models import (
    Task,
    Order,
)


class TaskSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'price',
            'done',
            'uri'
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-task:task_details", kwargs={"id": obj.id}, request=request)


class OrderSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    task = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.filter(done=False),
    )
    task_name = TaskSerializer(
        source='task',
        read_only=True,
    )

    class Meta:
        model = Order
        fields = (
            'id',
            'task',
            'user',
            'task_name',
            'open',
            'date',
            'uri',
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-task:order_details", kwargs={"id": obj.id}, request=request)
