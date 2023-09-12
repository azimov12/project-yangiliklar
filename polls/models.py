from django.db import models
from datetime import datetime
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    news_about = models.CharField(max_length=100)
    content = models.TextField()
    posted_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_about