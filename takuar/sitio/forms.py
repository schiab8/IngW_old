from django import forms
from sitio.models import Event


from django.contrib.admin.widgets import AdminDateWidget
class FormEvent(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']
        widgets = {'startTime': AdminDateWidget()}
