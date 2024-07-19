from django.db import models

# Create your models here.
from django.db import models

class SearchHistory(models.Model):
    user = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=1)
