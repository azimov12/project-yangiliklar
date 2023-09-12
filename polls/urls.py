from django.urls import path
from .views import (AllNewsCategories, DetailNewsCategory, CreateNewsCategory, UpdateNewsCategory, DeleteNewsCategory,
                    AllNews, DetailNews, CreateNews, UpdateNews, DeleteNews, NewsByCategory)

urlpatterns = [
    path('all-categories/', AllNewsCategories.as_view()),
    path('detail-category/int:<category_id>', DetailNewsCategory.as_view()),
    path('create-category/', CreateNewsCategory.as_view()),
    path('update-category/int:<category_id>', UpdateNewsCategory.as_view()),
    path('delete-category/int:<category_id>', DeleteNewsCategory.as_view()),
    path('all-news/', AllNews.as_view()),
    path('detail-news/int:<news_id>', DetailNews.as_view()),
    path('create-news/', CreateNews.as_view()),
    path('update-news/int:<news_id>', UpdateNews.as_view()),
    path('delete-news/int:<news_id>', DeleteNews.as_view()),
    path('category-news/int:<category_id>', NewsByCategory.as_view()),
]                    