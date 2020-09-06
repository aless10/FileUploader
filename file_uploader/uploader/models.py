import uuid

from django.db import models


class Link(models.Model):
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    password = models.CharField(max_length=16, null=True)
    expiry_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)


class File(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField()
    link = models.ForeignKey("Link", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
