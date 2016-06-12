from django.shortcuts import render
from sitio.models import Event, EventComment, Picture, UserProfile, Invitation, Group, Meeting
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from sitio.forms import FormEvent, FormEventComment, FormReportUser, FormGroup, FormInvitation
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from datetime import datetime

from django.forms import modelformset_factory


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
        mi_form = FormEvent(initial={'organizer':request.user})
    else:
        mi_form = FormEvent(request.POST)
        if mi_form.is_valid():
            mi_form.save()
            return HttpResponseRedirect('/')

    return render(request, 'addEvent.html', {'form_event': mi_form})


def detailsEvent(request):
    try:
        event = Event.objects.get(pk=request.GET['event'])
        event_comments = EventComment.objects.filter(event=event)
    except ObjectDoesNotExist:
        event = None
    if event is None:
        return HttpResponse('No existe el evento')

    if request.method == "GET":
        now = datetime.now()
        form = FormEventComment(initial={'user': request.user, 'submit_date': now, 'event':event})
        return render(request, 'infoEvent.html', {'event':event, 'form_comment': form, 'comments': event_comments})
    else:
        form = FormEventComment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Comentario posteado')
        return render(request, 'infoEvent.html', {'event':event, 'form_comment': form, 'comments': event_comments})

def reportUser(request):
    if request.method == "GET":
        now = datetime.now()
        reported = User.objects.get(pk=request.GET['user'])
        form = FormReportUser(initial={'reporter':request.user, 'submit_date':now, 'reported': reported})
        return render(request, 'reportUser.html', {'form':form, 'reported':reported})
    else:
        form = FormReportUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reporte enviado')
        return render(request, ' reportUser.html', {'form':form, 'reported':reported})
        
def userProfile(request):
    if request.method == "GET":
        data = {}
        if 'user' in request.GET:
            user_profile = UserProfile.objects.get(userAuth__username=request.GET['user'])
        else:
            user_profile = UserProfile.objects.get(userAuth=request.user)
            groups = Group.objects.filter(creator=request.user)
            data['groups']=groups
        data['userProfile']=user_profile
        return render(request, 'user_profile.html', data)

def newGroup(request):
    if request.method == "GET": 
        form = FormGroup(initial={'creator':request.user})
    else:
        form = FormGroup(request.POST)
        if form.is_valid():
            group = Group(creator=request.user, event=form.cleaned_data['event_select'])
            group.save()
            invitation = Invitation(group=group, userAuth=form.cleaned_data['user_select'])
            invitation.save()
            return HttpResponse('Grupo creado')
    return render(request, 'newGroup.html', {'form':form})
        

def searchUser(request):
    if request.method == "GET":
        user_list = UserProfile.objects.filter(userAuth__username__startswith=request.GET['text'])
        return render(request, 'user_list.html',{'user_list':user_list})

def getInvitations(request):
    if request.method == "GET":
        invitations=Invitation.objects.filter(userAuth=request.user, accepted=False)
        return render(request, 'invitation_list.html', {'invitations':invitations})

def acceptInvitation(request):
    if request.method == "POST":
        try: 
            id = request.POST.get('invitation_id')
            invitation = Invitation.objects.get(pk = id)
            print "invitation:", invitation
            if invitation.userAuth == request.user:
                invitation.accepted = True
                invitation.save()
                print "Todos confirmados:", invitation.group.checkConfirmed()
                group = invitation.group
                if invitation.group.checkConfirmed():
                    # Busco grupos iguales. Si hay, creo una meeting y la agrego a los dos grupos. Excluyo mi grupo
                    possible_groups = Group.objects.filter(allConfirmed=True).filter(waiting=True).exclude(pk=group.pk)
                    if possible_groups.count()>0:

                        other = possible_groups[0]

                        meeting = Meeting()
                        meeting.save()
                        group.meeting = meeting
                        other.meeting = meeting

                        group.waiting=False
                        other.waiting = False
                        group.save()
                        other.save()
                        print "Grupo encontrado"
                        return HttpResponse('Grupo encontrado: ', other)
                    else:
                        print "Esperando coincidencias"
                        return HttpResponse('Esperando coincidencias')
                print  "Aceptada, pero no todos confirmaron"
                return HttpResponse('OK!')
            print "El usuario no corresponde al gupo"
            return HttpResponse('El usuario no corresponde al grupo')
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            print "Error alguno"
            return HttpResponse('Error')
