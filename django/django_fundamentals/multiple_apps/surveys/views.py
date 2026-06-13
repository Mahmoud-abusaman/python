from django.shortcuts import render, HttpResponse

# Create your views here.
def get_all_surveys(request):
    return HttpResponse("all surveys")

def new_survey(request):
    return HttpResponse("new survey")
