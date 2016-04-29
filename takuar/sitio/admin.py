from django.contrib import admin
from sitio.models import UserProfile, Picture, UserType, Gender, Event, Local, LocalType

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(UserType)
admin.site.register(Gender)

admin.site.register(Event)
admin.site.register(Local)
admin.site.register(LocalType)
