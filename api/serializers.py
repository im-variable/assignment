from rest_framework import serializers
from .models import ImageData
from django import forms


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageData
        fields = '__all__'