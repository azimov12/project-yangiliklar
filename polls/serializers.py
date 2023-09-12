from .models import NewsCategory, News
from rest_framework import serializers

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['name','id']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_about', 'content', 'posted_at', 'category']