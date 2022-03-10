from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
def home(request):
    return render(request, 'check_noshow/home.html',
                    {"cur_time": datetime.now()})
