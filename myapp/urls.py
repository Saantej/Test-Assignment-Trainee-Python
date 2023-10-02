from django.urls import path
from . import views

urlpatterns = [
    # URL для списка уроков доступных пользователю
    path('lessons/', views.LessonListAPIView.as_view(), name='lesson-list'),

    # URL для списка уроков конкретного продукта, к которому есть доступ
    path('products/<int:product_id>/lessons/', views.ProductLessonListAPIView.as_view(), name='product-lesson-list'),

    # URL для статистики по продуктам
    path('product-stats/', views.ProductStatsAPIView.as_view(), name='product-stats'),

    # Добавьте другие URL-маршруты здесь, если есть

]