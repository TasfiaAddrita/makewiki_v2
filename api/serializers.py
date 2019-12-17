from rest_framework.serializers import ModelSerializer
from wiki.models import Page

class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'created', 'author']

class PageDetailSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'