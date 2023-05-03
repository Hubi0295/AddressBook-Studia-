from django.shortcuts import render, redirect
from Address.models import Voivodeship, Address
from .forms import SignupForm
# Create your views here.
def index(request):
    addresses = Address.objects.all()
    voivodeships = Voivodeship.objects.all()
    return render(request,'core/index.html',{
        'voivodeships': voivodeships,
        'addresses':addresses,
    })
def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html',{
        'form':form
    })