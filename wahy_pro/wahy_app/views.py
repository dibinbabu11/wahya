from django.shortcuts import render,get_object_or_404,redirect
from . models import Category,Product
from . forms import ProductForm


# Create your views here.


def index(request):
    product=Product.objects.all()

    return render(request,'index.html',{'product':product})


def category_view(request,c_slug=None):
    categorys = None
    if c_slug != None:
       categorys = get_object_or_404(Category,slug=c_slug)
       product      = Product.objects.filter(Category=categorys)
      
    else:
        product=Product.objects.all()

    
    return render(request,'category.html',{'categorys':categorys ,'product':product})

def detail(request,id):
    product=Product.objects.get(id=id)
    return render (request,'detail.html',{'product':product})

def add(request):
    form=ProductForm()
    if request.POST:
        name=request.POST.get('name')
        descr =request.POST.get('descr')
        price=request.POST.get('price')
        category =request.POST.get('category')
        image=request.POST.get('image')
        available=request.POST.get('available')
        stock=request.POST.get('stock')
        product=Product(name=name,descr=descr,price=price,category=category,image=image,available=available,stock=stock)
        product.save()

    return render(request,'add.html',{'form':form})

def edit(request,id):
    product=Product.objects.get(id=id)
    form=ProductForm(request.POST or None , request.FILES ,instance=product)
    if form.is_valid():
        form.save
        return redirect('/')

    return render(request,'edit.html',{'form':form,'product':product})

def delete(request,id):
    if request.method=='POST':
        product=Product.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request,'delete.html')
