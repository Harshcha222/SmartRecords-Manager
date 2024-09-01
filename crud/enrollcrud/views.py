from django.shortcuts import render, HttpResponseRedirect
from .forms import studentform
from .models import user

def add(request):
    if request.method == 'POST':
        fm = studentform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = studentform()
    
    stu = user.objects.all()
    return render(request, 'enrollcrud/addshow.html', {'form': fm, 'stude': stu})

def delete(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    pi = user.objects.get(pk=id)
    if request.method == 'POST':
        fm = studentform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
              
    else:
        pi=user.objects.get(pk=id)
        fm=studentform(instance=pi)
    
    return render(request, 'enrollcrud/updatestudent.html', {'form': fm})





# Create your views here.
 