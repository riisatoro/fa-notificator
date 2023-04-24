from django.db import models


class InternalAccessToken(models.Model):
    service = models.CharField(max_length=100, unique=True)
    token = models.TextField(unique=True)
