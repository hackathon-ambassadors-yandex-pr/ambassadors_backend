from django.db import models


class Address(models.Model):
    address = models.CharField()
