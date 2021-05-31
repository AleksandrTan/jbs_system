from django.forms import ModelForm
from mainsystem.models import TestData


class TestForm(ModelForm):
    class Meta:
        model = TestData
        fields = ['firstname', 'lastname', 'email', 'cv_data', 'cv_file_name', 'ai_resume_builder', 'dropbox_cv_url',
                  'upload_file', 'copy_paste', 'authenticity_token']
