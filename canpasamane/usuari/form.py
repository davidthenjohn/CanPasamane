
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuari.models import Usuari
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ["first_name","email" , "password1", "password2"]
    def clean(self):
        nom_usuari = self.cleaned_data['email']
        user = User.objects.filter(username=nom_usuari).count()
        if user > 0:
            raise ValidationError("El usario ya existe")
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data['email']
        user.firts_name = self.cleaned_data['first_name']
        

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ('telefon', 'pais')
