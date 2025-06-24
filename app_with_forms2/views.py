from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer


# Create your views here.

def customer_form(request):
    form = CustomerForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('customers_list')
    ctx = {
        'form': form
    }
    return render(request, 'form.html', ctx)


def customers_list(request):
    customers = Customer.objects.all()
    ctx = {
        'customers': customers
    }
    return render(request, 'table.html', ctx)




# Create your views here.
