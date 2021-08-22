from django.conf import settings
from django.db import models


class Email(models.Model):
    spf = models.CharField(max_length=254, null=True)
    dkim = models.CharField(max_length=254, null=True)
    html = models.TextField(null=True)
    text = models.TextField(null=True)
    subject = models.CharField(max_length=254, null=True)
    headers = models.TextField(null=True)
    content = models.TextField(null=True)
    to_email = models.CharField(max_length=254, null=True)
    charsets = models.JSONField()
    envelope = models.JSONField()
    sender_ip = models.CharField(max_length=254, null=True)
    spam_score = models.FloatField(null=True)
    from_email = models.CharField(max_length=254, null=True)
    spam_report = models.CharField(max_length=254, null=True)


class Attachment(models.Model):
    type = models.CharField(max_length=254)
    file = models.FileField(upload_to=settings.EMAIL_ATTACHMENT_UPLOAD_PATH)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    filename = models.CharField(max_length=254)
    content_id = models.CharField(max_length=254)


class RequestLog(models.Model):
    data = models.TextField()
    path = models.CharField(max_length=254)
    query = models.CharField(max_length=254)
    method = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
