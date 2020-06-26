from django.shortcuts import render
from .models import Covid
from django.db.models import Count, Q
import pandas as pd

def home(request):
    return render(request, 'home.html')

def world_population(request):
    return render(request, 'world_population.html')

def ticket_class_view_1(request):  # 방법 1
    dataset = pd.read_csv('C:\work\covid\countries-aggregated.csv')
    return render(request, 'ticket_class_1.html', {'dataset': dataset})

def ticket_class_view_2(request):  # 방법 2
    dataset = pd.read_csv('C:\work\covid\countries-aggregated.csv')
    return render(request, 'ticket_class_2.html', {'dataset': dataset})

def ticket_class_view_3(request):  # 방법 3
    dataset = pd.read_csv('C:\work\covid\countries-aggregated.csv')
    return render(request, 'ticket_class_3.html', {'dataset': dataset})

def json_example(request):  # 방법 4
    pass

def chart_data(request):  # 방법 4
    pass