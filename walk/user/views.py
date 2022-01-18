from django.shortcuts import render


# Create your views here.
def profile(request):
    """ creates the user profile page view """
    return render(request, 'user/profile.html')
