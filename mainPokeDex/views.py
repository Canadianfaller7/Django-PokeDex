import imp
from django.shortcuts import render

def home(request):
    return render(request, 'PokeDex/PokeDex_home.html')