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
from django.conf.urls import url, patterns, include
from django.contrib import admin 
from django.contrib.auth import views
from django.views.generic.edit import CreateView

from django.conf import settings

from users.views import user_registration_view
from sitio.views import userProfile

from users.forms import UserRegisterForm
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'sitio.views.home'),
    url(r'^login', views.login, {'template_name':'login.html'}),
    url(r'^logout/', views.logout, {'template_name':'logout.html'}),
    url(r'^register/', user_registration_view, name='registration'),
    url(r'^addEvent/', 'sitio.views.addEvent'),
    url(r'^test/', 'sitio.views.test'),
    url(r'^details', 'sitio.views.detailsEvent'),
    url(r'reportUser','sitio.views.reportUser'),
    url(r'^profile/', userProfile),
    url(r'^newGroup', 'sitio.views.newGroup'),
	url(r'^detallesGrupo', 'sitio.views.detalles_grupo'),
    url(r'^search_user','sitio.views.searchUser'),
    url(r'^get_events', 'sitio.views.getEvents'),
    url(r'^get_invitations', 'sitio.views.getInvitations'),
    url(r'^forum','forum.views.forumHome'),
    url(r'^thread','forum.views.viewThread'),
    url(r'^invitation_accept/', 'sitio.views.acceptInvitation'),
    url(r'^flag/', 'forum.views.flagReply'),
    #Haystack
    url(r'^search/', include('haystack.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
