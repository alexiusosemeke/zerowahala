from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View
from .forms import VentForm
from .models import Vents

# Create your views here.

@login_required
def submit_vent(request):
    if request.method == 'POST':
        ventForm = VentForm(request.POST)

        if ventForm.is_valid():
            vent = ventForm.save(commit=False) # this means that it should save the form but don't add to the database yet because the vent data is not being tied to a user yet
            vent.user = request.user # here we are not assigning the current logged in user to this vent data
            vent.save() # then we now save it
            messages.success(request, message='Released! Your mind is clearer already')
            return redirect('accounts:home')
    else:
        ventForm = VentForm()
    return render(request, 'accounts/home.html', {'ventForm': ventForm})
