from django.db.models import Count, Sum, Q, ExpressionWrapper, FloatField
from django.db.models.functions import Coalesce
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Lesson, Product, User
from .serializers import LessonSerializer, ProductStatsSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        accessible_lessons = Lesson.objects.filter(products__productaccess__user=user)
        return accessible_lessons

class ProductLessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        accessible_lessons = Lesson.objects.filter(products__productaccess__user=user, products__id=product_id)
        return accessible_lessons


class ProductStatsAPIView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer


    def get_queryset(self):
        total_users = User.objects.count()
        queryset = Product.objects.annotate(
            total_lessons_viewed=Count('lessons__lessonviewhistory__is_viewed', filter=Q(lessons__lessonviewhistory__is_viewed=True)),
            total_watch_time=Sum('lessons__duration_seconds'),
            student_count=Count('productaccess__user', distinct=True),
        ).annotate(
            purchase_percentage=ExpressionWrapper(
                Coalesce(Count('productaccess__id'), 0) * 100.0 / total_users,
                output_field=FloatField()
            )
        )

        return queryset