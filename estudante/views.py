from django.shortcuts import render
from .models import Estudante
from .forms import EquipeForm

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