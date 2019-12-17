from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 
from django.shortcuts import get_object_or_404

from wiki.models import Page
from .serializers import PageSerializer, PageDetailSerializer

# Create your views here.
class PageList(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.ListAPIView):
    pass
    # queryset = Page.objects.all()
    # serializer_class = PageDetailSerializer

    # model = Page
    # def get(request, id):
    #     page = queryset.get(pk=id)