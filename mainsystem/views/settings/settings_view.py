from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from rest_framework.views import APIView

from mainsystem.views.basepage import BaseAdminView
from mainsystem.models import Settings
from mainsystem.forms.settings_form import SettingsForm


class SettingsView(BaseAdminView, ListView):
    """
    Get page for view proxy
    """
    template_name = 'settings/settings.html'
    model = Settings


class CreateSettings(BaseAdminView, TemplateView):
    template_name = "settings/create_settings.html"

    def post(self, request, *args, **kwargs):
        settings_form = SettingsForm(request.POST, request.FILES)
        if settings_form.is_valid():
            proxy = settings_form.save()
            return redirect('settings_view')
        else:
            return render(request, "settings/create_settings.html", {"form": settings_form})


class UpdateSettings(BaseAdminView, APIView):
    def get(self, request, *args, **kwargs):
        if request.is_ajax() and self.request.GET.get('id_data'):
            print(self.request.GET.get('id_data'))
            is_active = True
            if is_active:
                return JsonResponse({'status': True})
            else:
                return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False})
