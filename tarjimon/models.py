from django.db import models

class Lugat(models.Model):
    english = models.CharField('english',max_length=30)
    uzbek = models.CharField('uzbek',max_length=30)