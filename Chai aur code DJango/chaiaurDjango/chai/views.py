from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.

def all_chai(request):
    ## fetching the data from db (now you can use chais everywhere.. at all_chai)
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    ## fetching the data from db (now you can use chai everywhere.. at all_chai)
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})
