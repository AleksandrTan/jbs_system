from django.core.validators import FileExtensionValidator
from django.db import models


class Portal(models.Model):
    alias = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Order(models.Model):
    portal = models.ForeignKey(Portal, on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    status_order = models.CharField(default="create", max_length=500)
    target_link = models.CharField(max_length=500, default='', blank=True)
    file_mailing = models.FileField(upload_to="files_mailing",
                                    validators=[FileExtensionValidator(['docx', 'doc', 'rtf', 'txt', 'pdf'],
                                                                       message="wrong file extension")])
    all_links = models.SmallIntegerField(default=0)
    send_links = models.SmallIntegerField(default=0)
    fail_links = models.SmallIntegerField(default=0)
    message = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
