from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import ImageSerializer
from .models import ImageData
import PIL
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.conf import settings
import os

class ImageView(APIView):
    def get(self, request, *args, **kwargs):
        qs = ImageData.objects.all()
        serializer = ImageSerializer(qs)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            img = os.path.abspath(settings.BASE_DIR) + serializer.data['image']
            image = PIL.Image.open(img)
            width, height = image.size
            context = {
                'image': serializer.data['image'].split('/')[-1], 
                'width': width, 
                'height': height
            }
            return JsonResponse(context)
        return Response(serializer.errors)