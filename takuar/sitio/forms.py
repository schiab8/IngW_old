from django import forms
from sitio.models import Event


class FormEvent(forms.ModelForm):
    class Meta:
        model = Event
        exclude = []
