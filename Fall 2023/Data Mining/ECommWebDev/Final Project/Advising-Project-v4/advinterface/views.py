# advinterface/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def profile_creation(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():

            # user_profile = form.save()

            return redirect('submission_successful')
    else:
        form = UserProfileForm()

    return render(request, 'advinterface/index.html', {'form': form})

def submission_successful(request):
    return render(request, 'advinterface/submit.html')
