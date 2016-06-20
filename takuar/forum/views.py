from django.shortcuts import render
from forum.models import Forum, Reply, Thread
from forum.forms import FormReply, FormThread
from django.http import HttpResponse

# Create your views here.

def forumHome(request):
    context = {}
    if 'id' in request.GET:
        forum = Forum.objects.get(pk=request.GET['id'])
        context['forum'] = forum
        context['threads'] = Thread.objects.filter(forum=forum).order_by('submit_date')
        context['form'] = FormThread(initial={'forum':context['forum'], 'author':request.user})
    else:
        context['forums'] = Forum.objects.all()
        return render(request, 'homeForum.html', context)
    if request.method == "POST":
        form = FormThread(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = FormThread()
    return render(request, 'forum.html', context)



def viewThread(request):
    context ={}
    if 'id' in request.GET:
        context['replies'] = Reply.objects.filter(thread__pk=request.GET['id']).order_by('submit_date')
        thread = Thread.objects.get(pk=request.GET['id'])
        context['thread'] = thread
        context['form'] = FormReply(initial={'thread':thread, 'author':request.user})
    else:
        return HttpResponse('ERROR')
    if request.method == "POST":
        form = FormReply(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['form'] = FormReply()
    return render(request, 'thread.html', context)

