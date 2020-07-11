from django.shortcuts import render, redirect
from .models import Show
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "GET":
        return redirect('/shows/new')
    if request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
    return redirect(f"/shows/{show.id}")

def display(request, id):
    show = Show.objects.get(id=id)
    show.release_date = show.release_date.strftime('%b %d, %Y')
    context = {
        "show": show
    }
    return render(request, 'show.html', context)

def shows(request):
    all_shows = Show.objects.all()
    for show in all_shows:
        show.release_date = show.release_date.strftime('%b %d, %Y')
    context = {
        "all_shows": all_shows
    }
    return render(request, 'all_shows.html', context)

def edit(request, id):
    show = Show.objects.get(id=id)
    show.release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        "show": show
    }
    return render(request, 'edit.html', context)

def update(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect(f"/shows/{show.id}")

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
