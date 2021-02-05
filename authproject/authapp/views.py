from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import SignupForm
def home(request):
    return render(request,'templateapp/home.html')
@login_required
def java(request):
    return render(request,'templateapp/java.html')
@login_required
def python(request):
    return render(request,'templateapp/python.html')
@login_required
def apti(request):
    return render(request,'templateapp/apti.html')
def logout(request):
    return render(request,'templateapp/logout.html')
def Signup(request):
    f=SignupForm()
    if request.method=='POST':
        f=SignupForm(request.POST)
        if f.is_valid():
            user=f.save()
            user.set_password(user.password)
            user.save()
            return redirect("/accounts/login")
    d={'form':f}
    return render(request,'templateapp/signup.html',d)
