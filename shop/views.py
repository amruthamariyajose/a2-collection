from django.shortcuts import render,get_object_or_404
# from django.views.generics.list import ListView
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request): 
    ca=categ.objects.all()
    paginator=Paginator(ca,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'cate':ca,'pg':pro})


def pr(request, c_slug=None):
    c_page=None
    
    if c_slug!=None:
        c_page=get_object_or_404(categ, slug=c_slug)
        # try:
        #     c_page = categ.objects.get(slug=c_slug)
        # except categ.DoesNotExist:
        #     print(Haiii)
    prod=products.objects.filter(category=c_page, available=True)
    
    paginator=Paginator(prod,3)
    try:
        page=int(request.GET.get('page','7'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    
    return render(request,'pm_index.html',{'pro':prod,'pg':pro})




def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'detail.html',{'pr':prod})


def searching(request):
    prod=None
    query=None
   
   
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    else:
        prod=products.objects.all()
    paginator=Paginator(prod,3)
    try:
        page=int(request.GET.get('page','7'))
    except:
        page=1
    try:
        
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    return render(request,'search.html',{'qr':query,'pr':prod,'pg':pro})



