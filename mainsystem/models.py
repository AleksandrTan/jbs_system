from django.core.validators import FileExtensionValidator
from django.db import models


class Order(models.Model):
    user_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    target_link = models.CharField(max_length=500, default='', blank=True)
    file_mailing = models.FileField(upload_to="files_mailing",
                                    validators=[FileExtensionValidator(['docx', 'doc', 'rtf', 'txt', 'pdf'],
                                                                       message="wrong file extension")])
    all_links = models.SmallIntegerField(default=0)
    send_links = models.SmallIntegerField(default=0)
    fail_links = models.SmallIntegerField(default=0)
    message = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
