from django.shortcuts import render, redirect
from .forms import MusicianModel_Form
from .models import Musician_Model

def add_musician(request):
    if request.method == 'POST':
        form = MusicianModel_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('add_album')
    else:
        form = MusicianModel_Form()
    context = {'form': form}
    return render(request, './musician_app/add_musician.html', context)


def edit_musician(request, musician_id):
    musician_from_db = Musician_Model.objects.get(pk=musician_id)
    form = MusicianModel_Form(instance=musician_from_db)
    if request.method == 'POST':
        form = MusicianModel_Form(request.POST, instance=musician_from_db)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    context = {'form': form}
    return render(request, './musician_app/edit_musician.html', context)


def delete_musician(request, musician_id):
    musician_from_db = Musician_Model.objects.get(pk=musician_id)
    musician_from_db.delete()
    return redirect('home')
