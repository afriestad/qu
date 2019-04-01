from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=127, null=False)
    course_code = models.CharField(max_length=16, null=False)
    semester = models.CharField(max_length=3, null=False)
    admins = models.ForeignKey(User, related_name='taught_courses', on_delete=models.DO_NOTHING)
    teaching_assistants = models.ForeignKey(User, related_name='assisted_courses', on_delete=models.DO_NOTHING)
    students = models.ForeignKey(User, related_name='taken_courses', on_delete=models.DO_NOTHING)
    year = models.DateField(default=now)


class Room(models.Model):
    name = models.CharField(max_length=127, null=False)

