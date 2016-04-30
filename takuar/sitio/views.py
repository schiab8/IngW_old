from django.shortcuts import render
from sitio.models import Event
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from sitio.forms import FormEvent
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime


# Create your views here.
def test(request): #Testeando Bootstrap
    return render(request, 'base.html')

@login_required
def home(request):
    now = datetime.now()
    events = Event.objects.filter(startTime__gte=now).order_by('-startTime')
    return render(request, 'inicio.html', {'events_list': events, 'user':request.user})

def addEvent(request):
    if request.method == "GET":
        mi_form = FormEvent(initial={"organizer":request.user})
    else:
        mi_form = FormEvent(request.POST)
        if mi_form.is_valid():
            mi_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'addEvent.html', {'form_event': mi_form})


def detailsEvent(request):
    if request.method == "GET":
        try:
            event = Event.objects.get(pk=request.GET['event'])
        except ObjectDoesNotExist:
            event = None
        if event is None:
            return HttpResponse('No existe el evento')
        else:
            return render(request, 'infoEvent.html',{'event':event})
        
