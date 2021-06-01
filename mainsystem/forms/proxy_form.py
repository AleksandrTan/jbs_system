from django.forms import ModelForm
from mainsystem.models import Proxy


class ProxyForm(ModelForm):
    class Meta:
        model = Proxy
        fields = ['protocol_proxy', 'host_proxy', 'port_proxy', 'username_proxy', 'password_proxy']
