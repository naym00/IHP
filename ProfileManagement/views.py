from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import ProfileInformation
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profileInformationPage(request):

    profile_list = ProfileInformation.objects.filter(user=request.user)

    if len(profile_list) != 0:
        profile = ProfileInformation.objects.get(user=request.user)
        form = ProfileForm(initial={'nickname': profile.nickname,})
    else:
        profile = None
        form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            instance = form.save(commit=False)
            instance.user = request.user



            if profile == None:
                instance.save()
            else:
                profile.nickname = instance.nickname
                profile.profilepic = instance.profilepic
                profile.coverpic = instance.coverpic
                profile.save()
            return redirect('profile')

    context = {
        'form' : form
    }
    return render(request, 'ProfileManagement/ProfileInformation.html', context)

@login_required
def profilePage(request):
    try:
        profile = ProfileInformation.objects.get(user=request.user)
    except ProfileInformation.DoesNotExist:
        profile = "Please complete your profile to view"

    context = {
        'profile': profile
    }
    return render(request, 'ProfileManagement/ProfileManagement.html', context)