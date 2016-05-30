from django import forms
from forum.models import Thread, Reply

class FormThread(forms.ModelForm):
    class Meta:
        model=Thread
        exclude=['submit_date']
        widgets = {'forum':forms.HiddenInput(),'author':forms.HiddenInput(),}

class FormReply(forms.ModelForm):
    class Meta:
        model=Reply
        exclude=['submit_date']
        widgets = { 'author': forms.HiddenInput(), 'thread': forms.HiddenInput(),}
