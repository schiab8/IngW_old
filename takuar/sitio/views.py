from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from django.db.models import Count

from datetime import datetime

from sitio.models import Event, EventComment, Picture, UserProfile, Invitation, Group, Meeting
from sitio.forms import FormEvent, FormEventComment, FormReportUser, FormGroup, FormInvitation
from forum.models import Forum, Thread


# Create your views here.
def test(request): #Testeando Bootstrap
    return render(request, 'base.html')

def home(request):
    now = datetime.now()
    events = Event.objects.filter(startTime__gte=now).order_by('-startTime')
    forums = Forum.objects.all().annotate(cant_threads=Count('thread')).order_by('-cant_threads')[:4]
    threads = Thread.objects.all().annotate(cant_replies=Count('reply')).order_by('-submit_date')[:4]
    return render(request, 'inicio.html', {'events_list': events, 'user':request.user, 'forums':forums, 'threads':threads})


@login_required
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

@login_required
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
            creator_of = Group.objects.filter(creator=request.user)
            member_of =  Group.objects.filter(invitation__userAuth=request.user)
            data['creator_of'] = creator_of
            data['member_of'] = member_of
        data['userProfile']=user_profile
        return render(request, 'user_profile.html', data)

def detalles_grupo(request):
    if request.method == "GET":
        id_grupo = request.GET.get('id_grupo')
        grupo = get_object_or_404(Group, id= id_grupo)
        #grupo = Group.objects.filter(id=id_grupo)
    else:
        id_grupo = request.POST.get('id_grupo')
        grupo = get_object_or_404(Group, id= id_grupo)
    return render(request, 'detalles_grupo.html', {'grupo':grupo})

@login_required
def newGroup(request):
    data = {}
    if request.method == "GET":
        if 'event' in request.GET:
            try:
                id = request.GET.get('event')
                event = Event.objects.get(pk = id)
                data['event'] = event

            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
        form = FormGroup()
    else:
        form = FormGroup(request.POST)
        if form.is_valid():
            guest_ids = list(set(form.cleaned_data['guests_ids'].split(',')))
            print guest_ids
            if 0<len(guest_ids)<5:
                users = User.objects.filter(pk__in = guest_ids)
                print users
                event_id = form.cleaned_data['event_id']
                group = Group(creator=request.user, event=Event.objects.get(pk=event_id))
                group.save()
                for id in guest_ids:
                    invitation = Invitation(group=group, userAuth=User.objects.get(pk=id))
                    invitation.save()
                return HttpResponse('Grupo creado')
    data['form'] = form
    return render(request, 'newGroup.html', data)


def searchUser(request):
    if request.method == "GET":
        user_list = UserProfile.objects.filter(userAuth__username__startswith=request.GET['text']).exclude(userAuth = request.user)
        return render(request, 'user_list.html',{'user_list':user_list})
def getEvents(request):
    if request.method == "GET":
        now = datetime.now()
        events = Event.objects.filter(startTime__gte=now).order_by('-startTime')
        print events
        return render(request, 'events_list.html', {'event_list':events})

@login_required
def getInvitations(request):
    if request.method == "GET":
        invitations=Invitation.objects.filter(userAuth=request.user, accepted=False)
        return render(request, 'invitation_list.html', {'invitations':invitations})

@login_required
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
