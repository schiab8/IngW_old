from django import forms
from sitio.models import Event


class FormEvent(forms.ModelForm):
    class Meta:
        model = Event
        exclude = []
        widgets = {
            'organizer':forms.HiddenInput(),
            }
            #'startTime': forms.DateTimeInput(format='%dd/%mm/%YYYY'),
