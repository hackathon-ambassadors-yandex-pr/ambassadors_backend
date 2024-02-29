from django.db import models


class Ambassador(models.Model):
    first_name = models.CharField()


class Adress(models.Model):
    address = models.CharField()
