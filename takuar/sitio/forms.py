from django import forms
from sitio.models import Event
from functools import partial


DateInput = partial(forms.DateInput, {'class':'datepicker'})

class FormEvent(forms.ModelForm):
    startTime = forms.DateField(widget=DateInput())
    finishTime = forms.DateField(widget=DateInput())

    class Meta:
        model = Event
        exclude = []
        widgets = {
            'organizer':forms.HiddenInput(),
            }
            #'startTime': forms.DateTimeInput(format='%dd/%mm/%YYYY'),
