from django.shortcuts import render, HttpResponse

# Create your views here.

def get_all_blogs(request):
    return HttpResponse("all blogs")

def get_blog_by_id(request, id):
    return HttpResponse(f"blog {id}")

def new_blog(request):
    return HttpResponse("new blog")

def edit_blog(request, id):
    return HttpResponse(f"edit blog {id}")

def delete_blog(request, id):
    return HttpResponse(f"delete blog {id}")