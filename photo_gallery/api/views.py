from django.shortcuts import render
from .serializers import ImageSerializer
from .models import ImageModel
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status


class ImageView(ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ImageModel.objects.all()
