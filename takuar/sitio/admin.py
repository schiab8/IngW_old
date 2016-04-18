from django.contrib import admin
from sitio.models import User, Picture, UserType, Gender, Event, Local, LocalType

# Register your models here.

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(UserType)
admin.site.register(Gender)

admin.site.register(Event)
admin.site.register(Local)
admin.site.register(LocalType)
