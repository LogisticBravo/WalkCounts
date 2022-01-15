from datetime import datetime
from django.shortcuts import render, redirect

from .forms import Goals_form
from .models import Goals


# Create your views here.
def steps(request):
    """ creates the steps target page view """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Goals_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            goals = form.cleaned_data['goals']
            g = Goals(goals=goals, submit_date=datetime.now())
            g.save()
            return redirect('home')
    else:
        form = Goals_form()
    return render(request, 'steps/steps.html', {'form': form})
