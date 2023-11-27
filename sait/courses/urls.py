from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson')
]
