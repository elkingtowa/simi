from django.db import models

class Send(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    send = models.ForeignKey(Send)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Poll(models.Model):
    # ...
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

class Choice(models.Model):
    # ...
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text

import datetime
from django.utils import timezone
# ...
class Poll(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)