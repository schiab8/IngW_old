from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

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

class UserProfile(models.Model):
    userAuth = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=50)
    profilePic = models.ForeignKey(Picture, blank=True, null=True)
    lastName = models.CharField(max_length=50)
    birth = models.DateTimeField()
    gender = models.ForeignKey(Gender, null=False, blank=False)
    idType = models.ForeignKey(UserType, null=False, blank=False)
    email = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=200, blank=True)

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
    picture = models.ForeignKey(Picture, blank=True, null=True)

class Group(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ForeignKey(Event)
    allConfirmed = models.BooleanField(default=False) #True cuando se confirman las invitaciones
    waiting = models.BooleanField(default=True) #False cuando se encuentra coincidencia de grupos
    meeting = models.ForeignKey(Meeting, blank=True, null=True)

    def __str__(self):
        return "Grupo de: %s" % self.creator
    
    def checkConfirmed(self):
        cant_invitations = Invitation.objects.filter(group=self).count()
        cant_accepted = Invitation.objects.filter(group=self).filter(accepted=True).count()
        if cant_invitations == cant_accepted:
            #Si estan todos confirmados cambio el estado  
            self.allConfirmed=True
            self.save()
            return True
        return False


class Invitation(models.Model):
    group = models.ForeignKey(Group)
    userAuth = models.ForeignKey(settings.AUTH_USER_MODEL)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return "Invitacion de %s a %s" % (self.group.creator, self.userAuth)

class Answer(models.Model): #Modelo temporalmente  en desuso. Los grupos se unen automaticamente sin aceptarse uno a otro
    group1 = models.ForeignKey(Group, null=False, blank=False, related_name='from+')
    group2 = models.ForeignKey(Group, null=False, blank=False, related_name='to')
    answer = models.BooleanField(default=False)
    
class Comment(models.Model):
    # ?
    # comment_object = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s") #Apunta al objeto donde se comento
    #object_type = GenericForeignKey(ct_field="content_type", fk_field="object_pk")#Tipo del objeto comentado
    user = models.ForeignKey(User, blank=True, null=True)
    comment = models.TextField(max_length=300)
    submit_date = models.DateTimeField(default=None)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return " %s, %s, %s" % (self.submit_date, self.user, self.comment)

class PictureComment(Comment):
    picture = models.OneToOneField(Picture)

    def __str__(self):
        return "Comentario sobre foto: %s" % comment

class EventComment(Comment):
    event = models.OneToOneField(Event)

    def __str__(self):
        return "Comentario sobre evento: %s" % comment


class UserReport(models.Model):
    reporter = models.OneToOneField(User, related_name='reporter')
    reported = models.OneToOneField(User, related_name='reported')
    submit_date = models.DateTimeField()
    report_message = models.TextField(max_length=300)

    def __str__(self):
        return "%s >> %s" % (self.reporter, self.reported)
