from django.forms import ModelForm
from mainsystem.models import Settings


class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        fields = ['alias', 'description']
