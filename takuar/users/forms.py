# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from sitio.models import Gender, UserType, UserProfile

class UserRegisterForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    profilePic = forms.ImageField(required=False)
    lastName = forms.CharField(min_length = 2, max_length=50)
    birth = forms.DateTimeField(widget=forms.SelectDateWidget(years=range(1950, 2016)))
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    email = forms.EmailField()
    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista otro usuario registrado con ese mismo email en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

    def clean_password2(self):
        """Comprueba que las passwords sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2
        
    def save(self):
        data = self.cleaned_data
        utype, created = UserType.objects.get_or_create(category='Usuario')
        userAuth = User(username=data['username'])
        userAuth.set_password(data['password'])
        userAuth.save()
        userProfile = UserProfile(userAuth = userAuth, name=data['name'], profilePic=data['profilePic'], lastName=data['lastName'],
            birth=data['birth'], gender=data['gender'], idType=utype, email=data['email'])
        userProfile.save()
        print "username: %s, password: %s, email: %s" % (userAuth, userAuth.password, userAuth.email)
        print "userProfile: %s" % userProfile
