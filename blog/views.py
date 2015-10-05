from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from forms import SignUpForm
from .forms import PostForm
# Create your views here.

#def main(request):
 #   return render_to_response('main.html', {}, context_instance=RequestContext(request))

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html',
                              context)

def explorarpost(request):
    context = RequestContext(request)
    return render_to_response('explorar-post.html',  context)

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
 
            return HttpResponseRedirect(reverse('app_blog:home'))  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))

def newpost(request):
        form = PostForm()
        return render(request, 'crear-post.html', {'form': form})
