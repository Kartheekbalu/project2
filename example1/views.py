from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def Home(request):
    post=Blog.objects.all()
    return render(request,'base.html',{'post':post})

def blog(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        date=request.POST['date']
        
        k=Blog(name=name,description=description,date=date)
        k.save()
    return render(request,'blog.html')

def update(request,id):
    post=Blog.objects.get(id=id)
    return render(request,'update.html',{'post':post})

def uprec(request,id):
    x=request.POST['name']
    y=request.POST['description']
    z=request.POST['date']
    post=Blog.objects.get(id=id)
    post.name=x
    post.description=y
    post.date=z
    post.save()
    return redirect('/')

def delete(request,id):
    rem=Blog.objects.get(id=id)
    rem.delete()
    return redirect('/')
    
def search(request):
    query=request.GET['q']
    data=Blog.objects.filter(name__icontains=query)
    return render(request, 'search.html',{'post':data})

