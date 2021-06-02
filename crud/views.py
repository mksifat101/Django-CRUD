from django.http.response import HttpResponseRedirect
from crud.forms import StudentRegister
from django.shortcuts import render
from .models import User


def add_show(request):
    if request.method == "POST":
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        fm = StudentRegister()
    else:
        fm = StudentRegister()
    stud = User.objects.all()
    return render(request, 'crud/addandshow.html', {'form': fm, 'stu': stud})


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = User.objects.get(pk=id)
            fm = StudentRegister(instance=pi)
    return render(request, 'crud/update.html', {'id': id})


def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
