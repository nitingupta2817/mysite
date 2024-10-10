from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from service.models import Service
from news.models import News

def homepage(request):
        
    return render(request,"index.html")

def about_us(request):
    if request.method=="GET":
        output=request.GET.get('output')
    
    return render(request, "aboutus.html",{'output':output})

def contactus(request):
    return HttpResponse("welcome to the world")

def courseDetail(request,Courseid):
    return HttpResponse("Courseid")

def aboutus(request):
    return HttpResponse("welcome to the world")

from django.shortcuts import render
from django.http import HttpResponseRedirect

def ankushpage(request):    
    return render(request,"ankush.html")

def creative(request):
       
    return render(request, "creative.html")




def practice(request):
    newsdata=News.objects.all()

    data = {        
        'newsdata': newsdata
    }

    return render(request, "practice.html", data)


def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="/":
                c=n1/n2

    except:
        c="invalid opr..."
        print(c)


    return render(request,"calculator.html", {'c':c})

def saveevenodd(request):  
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="even number"
        else:
            c="odd number"  
    return render(request,"saveevenodd.html", {'c':c})

def marksheet(request):   
    if request.method=="POST":
        if request.POST.get('subject1')=="":
            return render(request,"marksheet.html", {'error': True})
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500;
        if p>=60:
            d="First"
        elif p>=48:
            d="secon"
        elif p>=35:
            d="thrid"
        else:
            d="fail"

        data={
            'total':t,
            'per':p,
            'div':d
        }
        return render(request,"marksheet.html", data)
    return render(request,"marksheet.html")


