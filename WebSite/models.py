from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=2000)
    date_input = models.DateTimeField(default=datetime.now, blank=True)