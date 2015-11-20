from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from forms import SignUpForm , UserProfileForm
from blog.models import Juego , Categoria , UserProfile , Comentario
from django.shortcuts import get_object_or_404
from django.db.models import Avg



# Create your views here.

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html',context)

def perfil(request):
    context = RequestContext(request)
    return render_to_response('perfil.html',context)

def explorarpost(request):
    context = RequestContext(request)
    posts = Juego.objects.filter(publicado = True)
    return render_to_response('explorar-post.html',
{'posts':posts},
context)

def signup(request):
    registered = False
    
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(data=request.POST)  # A form bound to the POST data
        profile_form = UserProfileForm(data=request.POST)
        
        if form.is_valid() and profile_form.is_valid():  # All validation rules pass
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
            registered = True
        else:
            print form.errors, profile_form.errors
            print("no pasa nada")
        new_user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
        login(request, new_user)
        return HttpResponseRedirect(reverse('app_blog:home'))  # Redirect after POST
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
 
    data = {
        'form': form,
        'profile_form': profile_form,
        'registered': registered,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))


@requires_csrf_token
def crear_juego(request):
    context = RequestContext(request)
    if request.method=='POST':
        game=Juego()
        game.titulo=request.POST['titulo']
        game.imagen=request.FILES['imagen']
        game.contenido=request.POST['contenido']
        game.resumen= request.POST['contenido'][0:100] + "..."
        game.url=request.POST['url']
        #game.categoria=request.POST.getlist('categorias')
        game.desarrollador=request.POST['desarrollador']
        game.plataformas = request.POST['plataformas']
        game.fechaCreacion=request.POST['fechaCreacion']
        game.autor = User.objects.get(id = request.user.id)
        game.save()
    else:
        print("NO crear_juego")
    
    return render_to_response('crear-post.html',  context)

@requires_csrf_token
def verjuego(request,id_post):
    context = RequestContext(request)
    post = Juego.objects.get(id=id_post)
    if request.method=="POST":  
        print("POST")
        asunto = request.POST["asunto"]
        autorComen = request.POST["autorComen"]
        contenido = request.POST["mensaje"]
        comentario=Comentario()
        juego = Juego.objects.get(id=id_post)
        comentario.autorComen = autorComen
        comentario.mensaje = mensaje
        comentario.post = juego
        comentario.save()
    else:
        print("NO verjuego")
    comentarios = Comentario.objects.filter(post=id_post)
    print(comentarios)
    res=Comentario.objects.filter(published_in=post).order_by('-fecha')
    avgEs=res.aggregate(Avg('valoracion'))['valoracion__avg']
    print(avgEs)
    if avgEs!=None:
        post.punt_media=avgEs
        post.save()
    return render_to_response('ver-post.html',{'post':post, 'comentarios':comentarios, 'avgEs':avgEs},context)

def enviar_comentario(request):
    context = RequestContext(request)
    valor = None 
    if request.method=="POST":
        print("POST1:"+str(request.POST))
        print("POST2:"+str(request.POST.keys()))
        asunto = request.POST["asunto"]
        autorComen = request.POST["autorComen"]
        mensaje=request.POST["mensaje"]
        print(request.POST["id"])
        juego = Juego.objects.get(id=request.POST["id"])
        comentario=Comentario()
        comentario.autorComen = User.objects.get(id = request.user.id)
        comentario.asunto = asunto
        comentario.mensaje = mensaje
        comentario.post = juego
        comentario.save()
        valor=Comentario.objects.filter(published_in=juego).order_by('-fecha')
    else:
        print("NO comentario")    
    comentarios = Comentario.objects.filter(post=request.POST['id'])    
    return render_to_response('comentario.html', 
                              {'comentarios':comentarios, 'valor':valor},
                              context)

