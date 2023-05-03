from django.shortcuts import render, get_object_or_404
from Address.models import Address
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    addresses = Address.objects.filter(created_by=request.user)
    return render(request,'dashboard/index.html', {
        'addresses':addresses,
    })
