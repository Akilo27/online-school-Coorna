from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_file = models.FileField(upload_to='videos')
    

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.course.title
