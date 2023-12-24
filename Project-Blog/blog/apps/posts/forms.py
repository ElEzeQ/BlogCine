from django import forms
from .models import Comentario

class Formulario_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)






