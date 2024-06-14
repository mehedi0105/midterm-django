from django.shortcuts import render
from Car.models import Post
from Brand.models import Brand
# Create your views here.
def home(request,category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Brand.objects.get(slug = category_slug)
        data = Post.objects.filter(brand_name  = category)
    categories = Brand.objects.all()
    return render(request,'home.html',{'data':data,'category':categories})


def buyNow(request,id,category_slug = None):
    data =Post.objects.all()
    if category_slug is not None:
        category = Brand.objects.get(slug = category_slug)
        data = Post.objects.filter(brand_name  = category)
    categories = Brand.objects.all()
    return render(request,'Car/profile.html',{'data':data,'category':categories,'idd':id})
