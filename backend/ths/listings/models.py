from django.db import models


class Listing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)