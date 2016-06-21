from django.contrib import admin
from sitio.models import UserProfile, Picture, UserType, Gender, Event, Local, LocalType, PictureComment, EventComment, Comment, UserReport, Group, Invitation, Meeting, ChatMessage

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(UserType)
admin.site.register(Gender)

admin.site.register(Event)
admin.site.register(Local)
admin.site.register(LocalType)
admin.site.register(Group)
admin.site.register(Invitation)
admin.site.register(Meeting)
admin.site.register(ChatMessage)


admin.site.register(Comment)
admin.site.register(PictureComment)
admin.site.register(EventComment)

admin.site.register(UserReport)
