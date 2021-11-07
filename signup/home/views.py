from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context ={
        'name':'sangmeshwar'
    }
    # return HttpResponse("This is home page!")
    return render(request,'index.html',context)

def login(request):
    return render(request,'login.html')
    # return HttpResponse("This is about page!")