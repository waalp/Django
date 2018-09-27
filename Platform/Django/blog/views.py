from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from blog.forms import UserForm

# Create your views here.

def login(request):
    person_list = User.objects.all()
    content = {'person_list':person_list}
    return render(request,'blog.html',content)


def regist(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('注册成功')
        else:
            return HttpResponse(form.errors)
    else:
        form = UserForm()
    return render(request,'regist.html',{'form':form})