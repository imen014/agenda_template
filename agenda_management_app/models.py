from django.db import models


class Agenda(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)