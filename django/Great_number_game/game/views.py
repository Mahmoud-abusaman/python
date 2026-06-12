from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import random
# Create your views here.
def members(request):

    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        if guess == request.session['number']:
            return render(request, 'index.html', {'message': 'You guessed the number!'})
        elif guess > request.session['number']:
            return render(request, 'index.html', {'message': 'Too high!'})
        else:
            return render(request, 'index.html', {'message': 'Too low!'})
    return render(request, 'index.html', {'message': 'Guess the number between 1 and 100'})

def reset(request):
    request.session.pop('number')
    return redirect('/')

