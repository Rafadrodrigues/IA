from django.shortcuts import render
from .models import Estudante
# Create your views here.

def index(request):
    
    #Consulta
    estudante = Estudante.objects.all()
    context = {
        'lista':estudante
    }
    return render(request,'estudante.html',context)
