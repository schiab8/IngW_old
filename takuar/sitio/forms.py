from django import forms
from sitio.models import Event, EventComment, UserReport, Group, Invitation
from django.contrib.auth.models import User
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

class FormEventComment(forms.ModelForm):
    class Meta:
        model = EventComment
        exclude = ['is_removed']
        widgets = {
                'user': forms.HiddenInput(),
                'submit_date': forms.HiddenInput(),
                'event': forms.HiddenInput(),
                }

class FormReportUser(forms.ModelForm):
    class Meta:
        model = UserReport
        exclude = []
        widgets = {
                'reporter':forms.HiddenInput(),
                'reported':forms.HiddenInput(),
                'submit_date':forms.HiddenInput(),
                }
        
class FormGroup(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        # invite = kwargs.pop('extra')
        super(FormGroup, self).__init__(*args, **kwargs)
        if args:
            for label, value in args[0].items():
                if label.startswith('user_'):
                    self.fields[label] = forms.IntegerField(value[0])

    def users(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('user_'):
                yield (self.fields[name].label, value)

class FormInvitation(forms.ModelForm):
    class Meta:
        model = Invitation
        exclude = []
