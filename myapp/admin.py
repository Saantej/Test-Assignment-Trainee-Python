from django.contrib import admin

from myapp.models import LessonViewHistory, User, Product, ProductAccess, Lesson

admin.site.register([User,Product, ProductAccess, Lesson, LessonViewHistory])