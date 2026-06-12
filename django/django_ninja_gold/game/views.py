from django.shortcuts import render, redirect
import random


dictionary = {
    'farm': {'start': 10, 'end': 20},
    'cave': {'start': 5, 'end': 10},
    'house': {'start': 2, 'end': 5},
    'casino': {'start': -50, 'end': 50},
}
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html',{'dictionary':dictionary})

def process_money(request):
    if request.method == 'POST':
        location = request.POST['location']
        if location == 'farm':
            num=random.randint(dictionary['farm']['start'], dictionary['farm']['end'])
            request.session['gold'] += num
            request.session['activities'].append(f'You earned {num} gold from the farm')
        elif location == 'cave':
            num=random.randint(dictionary['cave']['start'], dictionary['cave']['end'])
            request.session['gold'] += num
            request.session['activities'].append(f'You earned {num} gold from the cave')
        elif location == 'house':
            num=random.randint(dictionary['house']['start'], dictionary['house']['end'])
            request.session['gold'] += num
            request.session['activities'].append(f'You earned {num} gold from the house')
        elif location == 'casino':
            num=random.randint(dictionary['casino']['start'], dictionary['casino']['end'])
            request.session['gold'] += num
            request.session['activities'].append(f'You earned {num} gold from the casino')
    return redirect('index')

def reset(request):
    request.session.flush()
    return redirect('index')