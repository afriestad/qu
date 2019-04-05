from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    template_name = 'course_admin/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'taken_courses': request.user.taken_courses.all(),
            'assisted_courses': request.user.assisted_courses.all(),
            'taught_courses': request.user.taught_courses.all()
        }

        return render(request, self.template_name, context=context)
