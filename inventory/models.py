from typing import Text
from django.db import models

# model for Ranks
class Inventory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=100000)
    def __str__(self):
        return self.name

