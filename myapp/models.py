from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True,null=True)

class Nested_Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    date=models.DateTimeField(auto_now_add=True,null=True)
