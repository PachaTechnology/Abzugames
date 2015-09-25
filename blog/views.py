from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
# Create your views here.
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)

def login(request):
    return render_to_response('login.html',
                              {})