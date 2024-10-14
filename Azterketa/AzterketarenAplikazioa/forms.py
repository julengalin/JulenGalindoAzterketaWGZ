from django import forms
from .models import Mediku,Paziente

class PazienteForm(forms.ModelForm):
    class Meta:
        model=Paziente
        fields=['id','izena','abizena', 'zita_data']

class MedikuForm(forms.ModelForm):
    class Meta:
        model= Mediku
        fields = ['id', 'izena', 'abizena']