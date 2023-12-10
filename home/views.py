from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        #Se o usuário for valido, carrega a página principal
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # preference = request.POST['preference']
        # user = authenticate(request, username=username, password=password,preference=preference)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/estudante') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'index.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})
 
def signup(request):
    if request.user.is_authenticated:
        return redirect("/estudante")
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request,"signup.html", {'form':form})
    
# def profile(request): 
#     return render(request, 'estudante.html')

# def home(request): 
#     return render(request, 'home.html')
 
def signout(request):
    logout(request)
    return redirect('/')