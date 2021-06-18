from django.core.validators import FileExtensionValidator
from django.db import models


class Portal(models.Model):
    alias = models.CharField(max_length=500, unique=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Order(models.Model):
    portal = models.ForeignKey(Portal, on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500, blank=True, default='')
    status = models.BooleanField(default=True)
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


class TestData(models.Model):
    firstname = models.CharField(max_length=500, blank=True)
    lastname = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    cv_data = models.CharField(max_length=500, blank=True)
    cv_file_name = models.CharField(max_length=500, blank=True)
    ai_resume_builder = models.BooleanField(default=False)
    dropbox_cv_url = models.CharField(max_length=500, default='', blank=True)
    upload_file = models.FileField(upload_to="files_test",
                                   validators=[FileExtensionValidator(['docx', 'doc', 'rtf', 'txt', 'pdf'],
                                                                      message="wrong file extension")])
    copy_paste = models.CharField(max_length=500, blank=True)
    authenticity_token = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Proxy(models.Model):
    protocol_proxy = models.CharField(max_length=500, default='', blank=True)
    host_proxy = models.CharField(max_length=500, default='', blank=True)
    port_proxy = models.SmallIntegerField(default=0, blank=True)
    username_proxy = models.CharField(max_length=500, default='', blank=True)
    password_proxy = models.CharField(max_length=500, default='', blank=True)
    is_active = models.BooleanField(default=False)
    fail_request_proxy = models.IntegerField(default=0)


class Settings(models.Model):
    alias = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

