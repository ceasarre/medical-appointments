from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm

from datetime import datetime
def home(request):
    return render(request, 'check_noshow/home.html',
                    {"cur_time": datetime.now()})

def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
    else:
        form = PersonForm()
    return render(request, 'check_noshow/person.html',
                        {"form": form})