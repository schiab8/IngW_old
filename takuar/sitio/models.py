from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=25)
    def __str__(self):
        return self.gender

class LocalType(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class UserType(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Picture(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=200)
    def __str__(self):
        return self.caption

class Group(models.Model):
    pass
    '''user1 =  models.ForeignKey(User, null=False, blank=False, related_name='creator')
    user2 =  models.ForeignKey(User, null=False, blank=False, related_name='second')
    user3 =  models.ForeignKey(User, null=True, blank=True, related_name='third')
    user4 =  models.ForeignKey(User, null=True, blank=True, related_name='fourth')
    user5 =  models.ForeignKey(User, null=True, blank=True, related_name='fifth')'''

class User(models.Model):
    name = models.CharField(max_length=50)
    profilePic = models.ForeignKey(Picture, blank=True)
    lastName = models.CharField(max_length=50)
    birth = models.DateTimeField()
    gender = models.ForeignKey(Gender, null=False, blank=False)
    idType = models.ForeignKey(UserType, null=False, blank=False)
    email = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    group = models.ManyToManyField(Group, blank=True)
    def __str__(self):
        return self.name +' '+ self.lastName

class Local(models.Model):
    name = models.CharField(max_length=20, default='Lugar')
    adress = models.CharField(max_length=50)
    capacity = models.IntegerField()
    idType = models.ForeignKey(LocalType, null=False, blank=False)
    def __str__(self):
        return self.name

class Event(models.Model):
    local = models.ForeignKey(Local, null=False, blank=False)
    eventName = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, null=False, blank=False)
    startTime = models.DateTimeField()
    finishTime = models.DateTimeField()
    def __str__(self):
        return self.eventName

class Meeting(models.Model):
    group = models.ManyToManyField(Group)
    picture = models.ForeignKey(Picture)
    event = models.ForeignKey(Event, null=False, blank=False)
    '''group1 = models.ForeignKey(Group, null=False, blank=False, related_name='+')
    group2 = models.ForeignKey(Group, null=False, blank=False, related_name='+')'''

class Answer(models.Model):
    group1 = models.ForeignKey(Group, null=False, blank=False, related_name='from+')
    group2 = models.ForeignKey(Group, null=False, blank=False, related_name='to')
    answer = models.BooleanField(default=False)