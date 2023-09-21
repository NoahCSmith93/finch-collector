from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    species = models.CharField(max_length=50)
    habitat = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def get_absolute_url(self):
        return reverse('finch_detail', kwargs={'pk': self.id})