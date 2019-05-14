# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit
# from usuari.models import User

# class UserCreationForm(forms.ModelForm):
#     contrasenya1 = forms.CharField(label="Contrasenya", widget=forms.PasswordInput)
#     contrasenya2 = forms.CharField(
#         label="Confirmar contrasenya", widget=forms.PasswordInput
#     )

#     class Meta:
#         model = User
#         fields = ("nom_user", "cognoms_user", "email" , "telefon", "pais")

#     def clean_contrasenya2(self):
#         contrasenya1 = self.cleaned_data.get("contrasenya1")
#         contrasenya2 = self.cleaned_data.get("contrasenya2")
#         if contrasenya1 and contrasenya2 and contrasenya1 != contrasenya2:
#             raise forms.ValidationError("Les contrasenyes no coincideixen")
#         return contrasenya2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)

#         user.set_pass(self.cleaned_data["contrasenya1"])
#         if commit:
#             user.save()
#         return user

# class UserChangeForm(forms.ModelForm):
#     class Meta:
#         Model = User
#         fields = ("telefon", "pais")

    
# class SignUpForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             "nom_user",
#             "contrasenya1",
#             "contrasenya2",
#             "email",
#             "telefon",
#             "pais",
#             Submit("signup", "Sign up"),
#         )

# class UpdateAccountForm(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#         super(UpdateAccountForm, self).__init__(*args, **kwargs)

#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             "telefon",
#             "pais",
#             Submit("update", "Actualitza perfil"),
#         )

# class ChangePasswordForm(PasswordChangeForm):

#     def __init__(self, *args, **kwargs):
#         user = kwargs["initial"]["user"]
#         super(ChangePasswordForm, self).__init__(user, *args, **kwargs)

#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             "old_pass",
#             "new_pass1",
#             "new_pass2",
#             Submit("update", "Actualitza contrasenya"),
#         )

# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)

#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             "email",
#             "contrasenya",
#             Submit("login", "Login"),
#         )