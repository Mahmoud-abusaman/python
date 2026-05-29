from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1

    return render(request, 'index.html')

def destroy(request):
    del request.session['visits']
    return redirect('/')
