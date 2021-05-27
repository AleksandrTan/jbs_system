from django.forms import ModelForm
from mainsystem.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['target_link', 'user_name', 'last_name', 'email', 'file_mailing']
