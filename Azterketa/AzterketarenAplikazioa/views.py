from django.shortcuts import redirect, render
from .models import Mediku, Mediku
from .forms import *
# Create your views here.
def paziente_list(request):
    pazienteZerrenda=Paziente.objects.all()
    return render(request, 'paziente_list.html',{'pazienteak':pazienteZerrenda})

def paziente_new(request):
    if request.method == 'POST':
        form=PazienteForm(request.POST)
        if form.is_valid:
            paziente = form.save()
            paziente.save()
        return redirect('paziente_zerrenda')
    else:
        form=PazienteForm()
        return render(request, 'paziente_new.html', {'form':form})
    
def ezabatu_paziente(request,id):
    pazienteEzabatu = Paziente.objects.get(id = id)

    Paziente.delete(pazienteEzabatu)

    return redirect('paziente_zerrenda')

def editpaziente(request, id):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        izena = request.POST.get("izena", "")
        abizena = request.POST.get("abizena", "")
        zita_data = request.POST.get("zita_data", "")
        paziente = Paziente.objects.get(id=id)
        paziente.izena = izena
        paziente.abizena = abizena
        paziente.zita_data = zita_data
        paziente.save()

        return redirect('paziente_zerrenda')
    
    else:
        pazienteZerrenda=Paziente.objects.all()
        return render(request, 'AzterketarenAplikazioa/paziente_edit.html',{'pazientea':pazienteZerrenda})

    
def mediku_list(request):
    medikuZerrenda=Mediku.objects.all()
    return render(request, 'mediku_list.html',{'medikuak':medikuZerrenda})

def mediku_new(request):
    if request.method == 'POST':
        form=MedikuForm(request.POST)
        if form.is_valid:
            mediku = form.save()
            mediku.save()
        return redirect('mediku_zerrenda')
    else:
        form=MedikuForm()
        return render(request, 'mediku_new.html', {'form':form})

def ezabatu_mediku(request,id):
    medikuEzabatu = Mediku.objects.get(id = id)
    
    Mediku.delete(medikuEzabatu)

    return redirect('mediku_zerrenda')

def edit_mediku(request, id):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        izena = request.POST.get("izena", "")
        abizena = request.POST.get("abizena", "")
        mediku = Mediku.objects.get(id=id)
        mediku.izena = izena
        mediku.abizena = abizena
        mediku.save()

        return redirect('mediku_zerrenda')
    
    else:
        medikuZerrenda=Mediku.objects.all()
        return render(request, 'AzterketarenAplikazioa/paziente_edit.html',{'medikua':medikuZerrenda})