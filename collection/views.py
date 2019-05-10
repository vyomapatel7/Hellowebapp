from django.shortcuts import render
from collection.models import Profile
# Create your views here.

def index(request):
    # defining the variable
    profiles = Profile.objects.all()
    return render(request, 'index.html', {
        'profiles': profiles,
    })

def profile_detail(request, slug):
    # grab the object...
    profile = Profile.objects.get(slug=slug)
    return render(request, 'profiles/profile_detail.html',{
        'profile': profile,
    })
