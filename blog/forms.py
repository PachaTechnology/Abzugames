from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Entrada, User
 
class SignUpForm(ModelForm):
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))
    class Meta:
        model = User
        fields = ['username', 'password1' , 'password2' , 'email' , 'first_name', 'last_name']
        widgets = {

            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('titulo', 'resumen', 'contenido', 'published', 'categoria')

