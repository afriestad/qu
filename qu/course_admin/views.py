from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    template_name = 'course_admin/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
