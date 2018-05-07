# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return "{}".format(self.text)
