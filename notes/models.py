from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


def note_time():
    return datetime.now() + timedelta(days=1)


class Notes(models.Model):
    NOTE_STATES = [(1, 'Active'), (2, 'Done'), (3, 'Postponed'), ]

    date = models.DateField(auto_now=True, verbose_name="Creation date")
    text = models.TextField(max_length=500, verbose_name="Text")
    is_public = models.BooleanField(verbose_name="Is public")
    is_important = models.BooleanField(verbose_name="Is important")
    finish_date = models.DateTimeField(default=note_time, verbose_name="End time")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Author")
    state = models.IntegerField(choices=NOTE_STATES, default=1)

    def __str__(self):
        return self.text
