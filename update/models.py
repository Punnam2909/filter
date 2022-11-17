from django.db import models

# Create your models here.
from django.views.generic import UpdateView


class addof(models.Model):
    name = models.CharField(max_length=120)
    class Meta:
        verbose_name = "addof"
        verbose_name_plural = "addofs"

    def __str__(self):
        return self.name


