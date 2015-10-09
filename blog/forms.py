from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Juego, User
 
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
<<<<<<< HEAD
=======

>>>>>>> 52c9beb1e0112d2b7b21eb828aed90335f547f7e
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        
<<<<<<< HEAD
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


            'password': forms.PasswordInput(),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ('titulo', 'contenido', 'imagen', 'categoria','url')
=======
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('titulo', 'resumen', 'contenido', 'published', 'categoria')
>>>>>>> 52c9beb1e0112d2b7b21eb828aed90335f547f7e

