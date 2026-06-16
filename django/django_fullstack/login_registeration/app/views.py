from django.shortcuts import render
import bcrypt
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def auth_page(request):
    return render(request, "auth.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(email=email).first()
        if user:
            try:
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    request.session['user_id'] = user.id
                    messages.success(request, "User logged in successfully")
                    return redirect('/dashboard')
            except ValueError:
                messages.error(request, "db error")
                return redirect('/')
        
        messages.error(request, "Invalid email or password")
        return redirect('/')
    return redirect('/')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        password = request.POST.get("password")
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        user = User.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            password=hashed_password,
        )
        
        request.session['user_id'] = user.id
        messages.success(request, "User created successfully")
        return redirect('/dashboard')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "dashboard.html", context)


def logout(request):
    request.session.flush()
    return redirect('/')
