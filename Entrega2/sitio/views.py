from django.shortcuts import render
from sitio.models import Event
from django.contrib.auth.decorators import login_required
from sitio.forms import FormEvent
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def home(request):
    events = Event.objects.all()
    return render(request, 'inicio.html', {'events_list': events, 'user':request.user})

def addEvent(request):
    if request.method == "GET":
        mi_form = FormEvent()
    else:
        mi_form = FormEvent(request.POST)
        if mi_form.is_valid():
            mi_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'addEvent.html', {'form_event': mi_form})