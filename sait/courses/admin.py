from django.contrib import admin
from .models import Course,Lesson,Enrollment,Teacher

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Teacher)
