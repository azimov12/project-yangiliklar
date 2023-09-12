from django.shortcuts import get_object_or_404
from .models import NewsCategory, News
from .serializers import NewsCategorySerializer, NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from rest_framework import status
# Create your views here.

class AllNewsCategories(APIView):
    def get(self, request):
        all_data = NewsCategory.objects.all()
        result = NewsCategorySerializer(all_data, many=True)
        return Response(result.data)

class DetailNewsCategory(APIView):
    def get(self, request, *args, **kwargs):
        categories = get_object_or_404(NewsCategory, id=kwargs['category_id'])
        serializer = NewsCategorySerializer(categories)
        print(7788787)
        return Response(serializer.data)

class CreateNewsCategory(APIView):
    def post(self, request):
        user_body = request.data
        serializer = NewsCategorySerializer(data=user_body)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)     
        return Response(serializer.errors)    

class UpdateNewsCategory(APIView):
    def patch(self, request, *args, **kwargs):
        categories = get_object_or_404(NewsCategory, id = kwargs['category_id'])
        serializer = NewsCategorySerializer(categories, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class DeleteNewsCategory(APIView):
    def delete(self, request, *args, **kwargs):
        categories = get_object_or_404(NewsCategory, id = kwargs['category_id'])
        categories.delete()
        return Response({'category':"successfully deleted"})   


class AllNews(APIView):
    def get(self, request):
        all_data = News.objects.all()
        result = NewsSerializer(all_data, many=True)
        return Response(result.data)

class DetailNews(APIView):
    def get(self, request, *args, **kwargs):
        news = get_object_or_404(News, id=kwargs['news_id'])
        serializer = NewsCategorySerializer(news)
        return Response(serializer.data)

class CreateNews(APIView):
    def post(self, request):
        body = request.data
        serializer = NewsSerializer(data=body)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)     
        return Response(serializer.errors)    

class UpdateNews(APIView):
    def patch(self, request, *args, **kwargs):
        news = get_object_or_404(NewsCategory, id = kwargs['news_id'])
        serializer = NewsSerializer(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class DeleteNews(APIView):
    def delete(self, request, *args, **kwargs):
        news = get_object_or_404(News, id = kwargs['news_id'])
        news.delete()
        return Response({'news':"successfully deleted"})   

class NewsByCategory(APIView):
    def get(self, request, category_id):
        try:
            category = NewsCategory.objects.get(id=category_id)
            news = News.objects.filter(category=category)
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)
        except NewsCategory.DoesNotExist:
            return Response(status=404)