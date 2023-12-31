from django.shortcuts import render
from .models import Estudante
from .forms import EquipeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    #Consulta
    estudante = Estudante.objects.all()
    context = {
        'lista':estudante
    }
    return render(request,'estudante.html',context)

def adicionar(request):
    form = EquipeForm()

    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = EquipeForm()
            return render(request,'adicionar_usuario.html', {'form':form})
        else:
            form = EquipeForm()

    return render(request,'adicionar_usuario.html',{'form':form})
# #Daqui para baixo foi tudo retirado do vídeo.
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})
   

# def signout(request):
#     logout(request)
#     return redirect('/')