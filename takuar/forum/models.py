from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=50)
    forum = models.ForeignKey(Forum)
    author = models.ForeignKey(User)
    submit_date = models.DateTimeField()

    def __str__(self):
        return '%s/%s de:%s. Fecha: %s' % (self.forum.name, self.name, self.author, self.submit_date)


class Comment(models.Model):
    author = models.ForeignKey(User)
    message = models.TextField(max_lenght=1000)
    submit_date = models.DateTimeField()
    
    def __str__(self):
        return 'Respuesta de %s. Fecha:%s' %(self.author, self.submit_date)
