from rest_framework import serializers
from .models import Documents


class DocumentSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Documents.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance