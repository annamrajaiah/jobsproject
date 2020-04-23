from django.shortcuts import render
from testapp.models import Hydjobs,Bengalorejobs,Delhijobs,punejobs

# Create your views here.
def home(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    list_hydjobs=Hydjobs.objects.all()
    my_dict={'list_hydjobs':list_hydjobs}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def bangalore_view(request):
    list_bgljobs=Bengalorejobs.objects.all()
    my_dict={'list_bgljobs':list_bgljobs}
    return render(request,'testapp/bgljobs.html',context=my_dict)
def delhijobs_view(request):
    list_delhijobs=Hydjobs.objects.all()
    my_dict={'list_delhijobs':list_delhijobs}
    return render(request,'testapp/delhijobs.html',context=my_dict)
def punejobs_view(request):
    list_punejobs=Hydjobs.objects.all()
    my_dict={'list_punejobs':list_punejobs}
    return render(request,'testapp/punejobs.html',context=my_dict)

