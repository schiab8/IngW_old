from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Thread(models.Model):
    name = models.CharField(max_length=50)
    forum = models.ForeignKey(Forum)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User)
    submit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s/%s de:%s. Fecha: %s' % (self.forum.name, self.name, self.author, self.submit_date)

class Reply(models.Model):
    author = models.ForeignKey(User)
    message = models.TextField(max_length=1000)
    submit_date = models.DateTimeField(auto_now=True)
    thread = models.ForeignKey(Thread)
    
    def __str__(self):
        return 'Respuesta de %s. Fecha:%s' %(self.author, self.submit_date)

class FlagReply(models.Model):
    reply = models.ForeignKey(Reply)
    userAuth = models.ForeignKey(User)
    submit_date = models.DateTimeField(auto_now=True)
