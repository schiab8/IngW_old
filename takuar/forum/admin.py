from django.contrib import admin
from forum.models import Forum, Thread, Reply

# Register your models here.
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Reply)
