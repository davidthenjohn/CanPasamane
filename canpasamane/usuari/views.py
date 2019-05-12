from __future__ import absolute_import
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse_lazy
from .models import User
from .form import SignUpForm, UpdateAccountForm, LoginForm, ChangePasswordForm
from .helpers import get_current_user

# Create your views here.
class UpdateAccountView(
    generic.UpdateView
):
    model = User
    form_valid_message = 'S\'conta actualitzada correctament.'
    form_class = UpdateAccountForm
    template_name = 'usuari/usuari_form.html'
    success_url = reverse_lazy('home')
    slug_field = 'nom_user'
    slug_url_kwarg = 'nom_user'

class ChangePasswordView(
    generic.FormView
):
    form_valid_message = 'La contrasenya ha sigut actualitzada'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')
    template_name = 'usuari/usuari_form.html'

    def form_valid(self, form):
        self.request.user.set_pass(form.cleaned_data['new_pass1'])
        self.request.user.save()

        return super(ChangePasswordView, self).form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        try:
            self.initial['user'] = self.request.user
        except AttributeError:
            raise Http404
        
        return super(ChangePasswordView, self).dispatch(
            request, *args, **kwargs)

class SignUpView(
    generic.CreateView
):
    model = User
    form_class = SignUpForm
    form_valid_message = 'Usuari creat correctament'
    success_url = reverse_lazy('usuari:login')
    template_name = 'usuari/usuari_form.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['signup'] = 'signup'

        return context

class LoginView(
    generic.FormView
):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    slug_url_kwarg = 'login'
    template_name = 'usuari/usuari_form.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['login'] = 'login'

        return context
    
    def form_valid(self, form):

        email = form.cleaned_data['email']
        contrasenya = form.cleaned_data['contrasenya']
        user = authenticate(email=email, contrasenya=contrasenya)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class ListAccountView():
    model = User
    template_name = 'usuari/usuari_list.html'
    context_object_name = 'users'
    
    def policy_view(request):
        return render(request, 'usuari/policy.html')

    @login_required
    def logout_view(request):
        logout(request)
        messages.success(request, 'Has sortit del perfil')
        return HttpResponseRedirect(reverse_lazy('home'))