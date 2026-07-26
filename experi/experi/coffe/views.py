from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

def all_coffe(request):
    coffis = ChaiVarity.objects.all()
    return render(request,'coffe/all_coffe.html',{'coffis':coffis})
def coffe_details(request,coffe_id):
    coffe = get_object_or_404(ChaiVarity,pk=coffe_id)
    return render(request,'coffe/coffe_details.html',{'coffe':coffe})