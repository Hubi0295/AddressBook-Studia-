from django.shortcuts import render,get_object_or_404,redirect
from .models import Address, Voivodeship
from django.contrib.auth.decorators import login_required
from .forms import NewAddressForm, EditAddressForm
from itertools import chain
# Create your views here.
def addresses(request):
    query=request.GET.get('query','')
    voivodeships=Voivodeship.objects.all()
    voivodeship_id=request.GET.get('voivodeship',0)
    addresses=Address.objects.all()
    if voivodeship_id:
        addresses=addresses.filter(voivodeship_id=voivodeship_id)
    if query:
        x=addresses.filter(first_name__icontains=query)
        y=addresses.filter(middle_name__icontains=query)
        z=addresses.filter(last_name__icontains=query)
        addresses=list(chain(x,y,z))
    return render(request, 'address/addresses.html',{
        'addresses':addresses,
        'query':query,
        'voivodeships':voivodeships,
        'voivodeship_id':int(voivodeship_id),
    })
def detail(request,pk):
    address = get_object_or_404(Address,pk=pk)
    return render(request,'address/detail.html',{
        'address':address
    })
@login_required
def new(request):
    if request.method == 'POST':
        form = NewAddressForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.save(commit=False)
            address.created_by = request.user
            address.save()
            return redirect('address:detail', pk=address.id)
    else:
        form = NewAddressForm()
    return render(request, 'address/form.html',{
        'form':form,
        'title':'Create New address!',
    })
@login_required
def delete(request, pk):
    address = get_object_or_404(Address,pk=pk,created_by=request.user)
    address.delete()
    return redirect('dashboard:index')
@login_required
def edit(request, pk):
    address = get_object_or_404(Address,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditAddressForm(request.POST, request.FILES, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address:detail', pk=address.id)
    else:
        form = EditAddressForm(instance=address)
    return render(request, 'address/form.html',{
        'form':form,
        'title':'Edit Address',
    })