from django.shortcuts import render
from django.http import HttpResponse

def hauntedmansiontwo(request):

    context = {}
    return render(request, 'hauntedmansiontwo.html', context)