from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from users.forms import UserRegisterForm
# Create your views here.

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    
    return render(request, 'register.html', context)
