from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_accesses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

class LessonViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_views')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_viewed = models.BooleanField()
