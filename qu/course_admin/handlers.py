from dataporten.models import DataportenUser
from allauth.account.signals import user_logged_in
from django.dispatch import receiver

from course_admin.models import Course


@receiver(user_logged_in)
def create_and_populate_courses(sender, request, user, **kwargs):
    # Ensure that user is a DataportenUser, or ignore the rest of this handler
    if not isinstance(user, DataportenUser):
        if DataportenUser.valid_request(request):
            user.__class__ = DataportenUser
            request.user.__class__ = DataportenUser
        else:
            return

    for code, dp_course in user.dataporten.courses.all.items():
        if dp_course.membership:
            course = None
            try:
                course = Course.objects.get(course_code=code, semester=dp_course.semester.season)
            except Course.DoesNotExist:
                course = Course.objects.create(
                    name=dp_course.name,
                    course_code=dp_course.code,
                    semester=dp_course.semester.season,
                )
            finally:
                if dp_course.membership.primary_affiliation == 'student':
                    course.students.add(user)
                elif dp_course.membership.primary_affiliation == 'teaching assistant':  # TODO: Fix this
                    course.teaching_assistants.add(user)
                elif dp_course.membership.primary_affiliation == 'admin':  # TODO: Fix this
                    course.admins.add(user)
                else:  # Fallback, assume student
                    course.students.add(user)
