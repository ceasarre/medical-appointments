from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person
from uuid import UUID

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
            return redirect("check-results")
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

def results(request):
    
    person = Person.objects.latest('created_at')
    time_delta = (person.date_of_appointment - person.date_of_set_appointment).days
    args = {
            "cur_time": datetime.now(),
            "person" : person,
            "timedelta" : time_delta
            }
    return render(request, 'check_noshow/results.html', args)