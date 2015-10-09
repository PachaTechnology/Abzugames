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
<<<<<<< HEAD
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


=======
            'password': forms.PasswordInput(),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('titulo', 'resumen', 'contenido', 'published', 'categoria')
>>>>>>> 10a1942eb906a899c3f2c813b9faf0d865cd3e4c
