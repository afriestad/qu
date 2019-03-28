from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=127, null=False)
    course_code = models.CharField(max_length=16, null=False)
    semester = models.CharField(max_length=3, null=False)
    admins = models.ForeignKey(User, on_delete=models.SET_NULL)
    teaching_assistants = models.ForeignKey(User, on_delete=models.SET_NULL)
    students = models.ForeignKey(User, on_delete=models.SET_NULL)
    year = models.DateField(default=now())


class Room(models.Model):
    name = models.CharField(max_length=127, null=False)

