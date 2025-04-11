from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from . models import*
from django.core.files.storage import FileSystemStorage
from django.core.serializers.json import DjangoJSONEncoder



def register(request):
    data=[]
    username=request.GET.get('username')
    password=request.GET.get('password')
    fullname=request.GET.get('name')
    place=request.GET.get('place')
    email=request.GET.get('email')
    phone=request.GET.get('phone')
    try:
        ob=Login.objects.filter(username=username)
        if ob:
            status = "error"
            message="Username Already Exists!!"
        else:
            obj=Login(username=username,password=password,usertype='user')
            obj.save()
            
            obj1=User(fullname=fullname,email=email,phone=phone,place=place,login_id=obj.pk)
            obj1.save()
            if obj1:
                status = "success"
            else:
                status = "error"
    except Login.DoesNotExist:
        status = "error"
        message="Failed"
        
    response = {
        
       'status': status,
        'data': data
    }
    if status == "error":
        response['message'] = message 
    
    return JsonResponse(response)






def user_login(request):
    data=[]
    username=request.GET.get('username')
    password=request.GET.get('password')

    print(username,password,"///////////////////++++++++++++++++++++++++")
    
    try:
        queryset=Login.objects.filter(username=username,password=password)
        for q in queryset:
            data.append({
                'login_id':q.login_id,
                'username':q.username,
                'password':q.password,
                'usertype':q.usertype
            })
        if data:
            status = "success"
        else:
            status = "error"
            message="Invalid credential"
            
    except Login.DoesNotExist:
        status = "error"
        message="Invalid credential"
        
    response = {
        
       'status': status,
        'data': data
    }
    print(data)
    
    if status == "error":
        response['message'] = message
        
    return JsonResponse(response)


