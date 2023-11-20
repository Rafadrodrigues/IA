from .models import Estudante
from django.forms import ModelForm

class EquipeForm(ModelForm):
    class Meta:
        model = Estudante
        fields = "__all__"