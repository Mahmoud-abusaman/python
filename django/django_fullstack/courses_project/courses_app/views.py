from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            new_desc = Description.objects.create(content=request.POST['description'])
            Course.objects.create(name=request.POST['name'], description=new_desc)
            messages.success(request, "Course successfully added!")
            return redirect('/')
    return redirect('/')

def destroy(request, id):
    # This renders the confirmation page
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "destroy.html", context)

def delete(request, id):
    # This actually deletes the course
    if request.method == "POST":
        course = Course.objects.get(id=id)
        # Deleting the course will also delete the description because of CASCADE
        course.delete()
        return redirect('/')
    return redirect('/')

def comments(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        Comment.objects.create(content=request.POST['content'], course=course)
        return redirect(f'/courses/{id}/comments')
    
    context = {
        "course": course,
        "comments": course.comments.all()
    }
    return render(request, "comments.html", context)
