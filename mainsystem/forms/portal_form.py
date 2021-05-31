from django.forms import ModelForm
from mainsystem.models import Portal


class PortalForm(ModelForm):
    class Meta:
        model = Portal
        fields = ['alias', 'name']
