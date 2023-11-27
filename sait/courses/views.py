from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment
import PIL

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def enroll(request, course_id):
    course = Course.objects.get(pk=course_id)
    Enrollment.objects.create(user=request.user, course=course)
    return redirect('course_detail', course_id=course_id)

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    check = course.enrollment_set.filter(user=request.user).exists
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons, 'check': check})

@login_required
def lesson_detail(request, lesson_id):
    lessons = Lesson.objects.get(id=lesson_id)
    return render(request, 'courses/lesson.html', {'lessons': lessons})
