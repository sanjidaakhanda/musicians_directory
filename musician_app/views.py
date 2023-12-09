from django.shortcuts import render, redirect
from .forms import MusicianForm
from .forms import MusicianInfo
from . import models 

def add_Musician(request):
    if request.method == "POST":
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('Musician')
    else:
        musician_form = MusicianForm()

    return render(request, 'Musician.html', {'form': musician_form})

def edit_Musician(request, id):
    musician = models.MusicianInfo.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)

    if request.method == "POST":
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
   

    return render(request, 'musician.html', {'form': musician_form})

def delete_musician(request, id):
    musician = models.MusicianInfo.objects.get(pk=id)
    musician.delete()
    return redirect('home')
