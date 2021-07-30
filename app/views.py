from django.shortcuts import render,redirect
from . models import blog
from . forms import blog_form

# Create your views here.

def Home(request):
    return render(request,"home.html")

def Post(request):
    if request.method=="POST":
        form=blog_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(Read)
        
    else:
        form=blog_form()
    return render(request,"post.html",{"form":form})

def Read(request):
    read=blog.objects.all()
    return render(request,"read.html",{"read":read})

def Update(request,id):
    upd= blog.objects.get(id=id)
    update=blog_form(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Read)
    return render(request,"update.html",{"update":update})

def Delete(request,id):
    del_t=blog.objects.get(id=id)
    del_t.delete()

    return redirect(Read)
    
    