from django.shortcuts import render
from django.http import HttpResponse


def all_coffe(request):
    return render(request,'coffe/all_coffe.html')
def mocca(request):
    return render(request,'coffe/mocca.html')