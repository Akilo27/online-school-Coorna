from django.contrib.auth.models import User
from django.db import models
from courses.models import Course



class Clans(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()

    def __str__(self):
        return self.course.title



class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=50)
    clans = models.ManyToManyField(Clans, related_name='clans')
    courses = models.ManyToManyField(Course, related_name='course')
