from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        created = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        messages.success(request, "Show successfully created!")
        return redirect(f'/shows/{created.id}')
    else:
        shows = Show.objects.all()
        return render(request, 'shows.html', {'shows': shows}) 

def add_new(request):
    return render(request, 'add_new.html')

def details(request, id):
    show = Show.objects.get(id=id)
    return render(request, 'details.html', {'show': show})

def update(request, id):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')
        
        messages.success(request, "Show updated successfully")
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
    else:
        show = Show.objects.get(id=id)
        return render(request, 'update.html', {'show': show})

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')