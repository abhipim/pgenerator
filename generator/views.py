from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'This is Password'})

def pwd(request):
    
    letters = 'qwertyuiopasdfghjklzxcbvnm'
    uppers = 'QWASZXEDCRFVTGBYHNUJMIKOLP'
    numbers = '0123456789'
    symbols = '~!@#$%^&*()_+}{|":?><`,./;[]\=-"}'

    upper,number,schar = 0,0,0

    length = int(request.GET.get('length'))
    if request.GET.get('Uppers'):
        upper = 1
    if request.GET.get('Numbers'):
        number = 1
    if request.GET.get('Special'):
        schar = 1

    source = letters + uppers*upper + numbers*number + symbols*schar
    generated = ''

    for i in range(length):
        generated+= random.choice(source) 

    
    return render(request,'generator/pwd.html',{'password':generated})
