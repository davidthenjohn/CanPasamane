

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuari.models import Usuari
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firts_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ["username", "email","firts_name", "password1", "password1"]
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email']
        user.firts_name = self.cleaned_data['firts_name']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuari
        fields = ('telefon', 'pais')
