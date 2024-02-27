from django.shortcuts import render,HttpResponse
from web.models import Service,Brand


def index(request):
    services=Service.objects.all()
    brands=Brand.objects.all()
    context={
        "services":services,
        "brands":brands
    }
    return render(request,'index.html',context=context)
