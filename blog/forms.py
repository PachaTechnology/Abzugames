from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import User , UserProfile
 
class SignUpForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['username', 'password' , 'email' , 'first_name', 'last_name',]
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']

        
