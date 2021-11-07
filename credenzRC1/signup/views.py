from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login as loginStudent
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.
def signupPage(request):
    if(request.method == 'POST'):
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        collegename = request.POST['collegeName']
        year = request.POST['year']
        password = request.POST['password']
        user = User.objects.create_user(username, '',password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        password = hash(password)
        attempt = 1
        signupEntry = Student(first_name=firstname,last_name=lastname,user_name=username,college_name=collegename,year_of_study=year,password=password)
        signupEntry.save()
        return render(request, 'home.html',{'username':username,'attempt':attempt,'disabled':'disabled'})
    return render(request,'signup.html')
        # return HttpResponse('This is signup page')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        attempt = 1
        if user is not None:
            loginStudent(request, user)
            return render(request,'home.html',{'username':username,'attempt':attempt,'disabled':'disabled'})
    # A backend authenticated the credentials
        else:
            return render(request,'login.html')
    # No backend authenticated the credentials
    return render(request,'login.html')

@login_required(login_url=None)
def home(request):
    return render(request, 'home.html')

@login_required(login_url=None)
def addResponse(request):
    if(request.method == 'POST'):
        Qid = request.POST['Qid']
        Answer = request.POST['answer']
        username = request.POST['username']
        attempt = request.POST['attempt']
        user = Student.objects.get(user_name = username)
        res = user.responses
        res[Qid] = [Answer,attempt]
        user.save()
        attempt = int(attempt) + 1
        return render(request, 'home.html',{'username':username,'attempt':attempt,'disabled':'disabled'})
    return render(request,'login.html')