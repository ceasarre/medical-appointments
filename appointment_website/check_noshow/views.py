from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person
from uuid import UUID
import numpy as np
import pandas as pd

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

def map_to_int(x):
    if x == True:
        return 1 
    else:
        return 0

def convert_handicap(x):
    if int(x) == 0:
        return np.array([1, 0, 0, 0, 0])
    elif int(x) == 1:
        return np.array([0, 1, 0, 0, 0])
    elif int(x) == 2:
        return np.array([0, 0, 1, 0, 0])
    elif int(x) == 3:
        return np.array([0, 0, 0, 1, 0])
    else:
        return np.array([0, 0, 0, 0, 1])
    


def results(request):
    
    person = Person.objects.latest('created_at')
    time_delta = (person.date_of_appointment - person.date_of_set_appointment).days
    data = []
    data.append(int(person.gender))
    data.append(int(person.age))
    data.append(map_to_int(person.scolarship))
    data.append(map_to_int(person.hipertension))
    data.append(map_to_int(person.diabetes))
    data.append(map_to_int(person.alcoholism))
    data.append(map_to_int(person.sms_received))
    data.append(int(person.num_app_missed))
    handicap = convert_handicap(person.handicap)
    # Add handicap to data - todo
    data = np.array(data)

    args = {
            "cur_time": datetime.now(),
            "person" : person,
            "timedelta" : time_delta,
            "data": data,
            "handicap": handicap
            }            
    
    return render(request, 'check_noshow/results.html', args)