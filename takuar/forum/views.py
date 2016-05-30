from django.shortcuts import render
from forum.models import Forum, Reply, Thread
from forum.forms import FormReply, FormThread
from django.http import HttpResponse

# Create your views here.

def forumHome(request):
    if request.method == "GET":
        if 'id' in request.GET:
            forum = Forum.objects.get(pk=request.GET['id'])
            threads = Thread.objects.filter(forum=forum).order_by('submit_date')
            form = FormThread(initial={'forum':forum, 'author':request.user})
            return render(request, 'forum.html', {'form':form,'threads':threads})
        forums = Forum.objects.all()
        return render(request, 'homeForum.html', {'forums':forums})
    else:
        form = FormThread(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Posteado')
        else:
            return HttpResponse(form.errors)


def viewThread(request):
    if request.method == "GET":
        if 'id' in request.GET:
            replies = Reply.objects.filter(thread__pk=request.GET['id']).order_by('submit_date')
            print replies
            thread = Thread.objects.get(pk=request.GET['id'])
            form = FormReply(initial={'thread':thread, 'author':request.user})
            return render(request, 'thread.html', {'form':form,'replies':replies, 'thread':thread})
    else:
        form = FormReply(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Posteado')
        else:
            return HttpResponse(form.errors)

