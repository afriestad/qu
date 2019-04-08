from django.apps import AppConfig


class CourseadminConfig(AppConfig):
    name = 'course_admin'

    def ready(self):
        import course_admin.handlers
