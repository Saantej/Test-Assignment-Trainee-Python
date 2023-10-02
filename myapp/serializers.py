# serializers.py

from rest_framework import serializers
from .models import Product, Lesson, LessonViewHistory

class LessonViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViewHistory
        fields = ('id', 'user', 'lesson', 'start_time', 'end_time', 'is_viewed')

class LessonSerializer(serializers.ModelSerializer):
    lessonviewhistory_set = LessonViewHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'video_url', 'duration_seconds', 'products', 'lessonviewhistory_set')

class ProductStatsSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.IntegerField()
    total_watch_time = serializers.IntegerField()
    student_count = serializers.IntegerField()
    purchase_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'total_lessons_viewed', 'total_watch_time', 'student_count', 'purchase_percentage')
