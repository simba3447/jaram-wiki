from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileView(TemplateView):
    template_name = 'main/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
