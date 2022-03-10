from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person

from datetime import datetime
def home(request):
    return render(request, 'check_noshow/home.html',
                    {"cur_time": datetime.now()})

def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        # save to database
        if form.is_valid():
            form.save()
            return redirect("check-history")
    else:
        form = PersonForm()
    return render(request, 'check_noshow/person.html',
                        {"form": form})

def history(request):
    return render(request, 'check_noshow/history.html',
                    {
                        "people": Person.objects.all(),
                        "num_people": Person.objects.count()
                    })