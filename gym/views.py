from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
from datetime import datetime

from django.utils import timezone

from gym.models import User,Contact

def LogIn(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.get(email=email)
            user_auth = authenticate(email=email, password=password)
            if user_auth is not None:
                login(request, user)
                return redirect("/homepage/")
            return redirect('/')
        except User.DoesNotExist:
            return redirect('/')
    return render(request, 'signIn.html')


def SignUp(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            date = request.POST.get("date")
            password = request.POST.get("password")
            date_object = datetime.strptime(date, "%Y-%m-%d")
            user = User.objects.create(email=email, sub_expired_on=date_object)
            user.set_password(password)
            user.save()
            return redirect("/")
        except Exception as e:
            return redirect("/signup/")
    return render(request, 'signUp.html')
        
def Homepage(request):
    today = timezone.now()
    show_plan = False
    user = request.user
    if user.is_authenticated:
        if user.sub_expired_on >= today:
            show_plan = True
        return render(request, "homepage.html", context={"show_plan": show_plan})
    return redirect("/")
def about(request):
    return render(request, 'about.html')    
# def contact(request):
#     return render(request, 'contact.html')  
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        message = request.POST.get("message")
        print(name,email,contact,message)
        data = Contact(name=name,contact=contact,email=email,message=message)
        data.save()
    return render(request, 'contact.html')    