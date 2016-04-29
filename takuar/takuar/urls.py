"""Entrega2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.edit import CreateView

from users.views import user_registration_view

from users.forms import UserRegisterForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'sitio.views.home'),
    url(r'^login', views.login, {'template_name':'login.html'}),
    url(r'^logout/', views.logout, {'template_name':'logout.html'}),
    url(r'^register/', user_registration_view, name='registration'),
    url(r'^addEvent/', 'sitio.views.addEvent'),
    url(r'^test/', 'sitio.views.test'),
    url(r'^details', 'sitio.views.detailsEvent'),
]
