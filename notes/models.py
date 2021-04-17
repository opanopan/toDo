from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class States(models.Model):
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state


class Notes(models.Model):
    date = models.DateField(auto_now=True, verbose_name="Creation date")
    text = models.TextField(max_length=500, verbose_name="Text")
    is_public = models.BooleanField(verbose_name="Is public")
    is_important = models.BooleanField(verbose_name="Is important")
    finish_date = models.DateTimeField(default=datetime.now()+timedelta(days=1), verbose_name="End time")
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, verbose_name="Author")
    state = models.ForeignKey(States, on_delete=models.PROTECT, verbose_name="State")

    def __str__(self):
        return self.text
