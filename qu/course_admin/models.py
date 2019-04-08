from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from dataporten.parsers import Semester


class Course(models.Model):
    name = models.CharField(max_length=127, null=False)
    course_code = models.CharField(max_length=16, null=False)
    semester = models.BooleanField(choices=[(Semester.AUTUMN, "Autumn"), (Semester.SPRING, "Spring")])
    admins = models.ManyToManyField(User, related_name='taught_courses')
    teaching_assistants = models.ManyToManyField(User, related_name='assisted_courses')
    students = models.ManyToManyField(User, related_name='taken_courses')
    year = models.DateField(default=now)


class Room(models.Model):
    name = models.CharField(max_length=127, null=False)

