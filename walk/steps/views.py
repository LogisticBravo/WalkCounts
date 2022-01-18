from datetime import date, timedelta
from django.shortcuts import render, redirect

from .forms import GoalsForm, StepsForm
from .models import Goals, Steps


# Create your views here.
def steps(request):
    """ creates the steps target page view """

    today = date.today()
    last_week = today - timedelta(days=7)
    monday_last = last_week - timedelta(days=(last_week.isocalendar()[2] - 1))
    this_monday = monday_last + timedelta(days=7)
    next_monday = this_monday + timedelta(days=7)
    form = GoalsForm()
    stepsform = StepsForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GoalsForm(request.POST)
        stepsform = StepsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            goals = form.cleaned_data['goals']
            first_name = request.user.first_name
            user = request.user.email
            g = Goals(goals=goals, submit_date=date.today(), first_name=first_name, user=user)
            g.save()
            return redirect('home')
        if stepsform.is_valid():
            steps_data = stepsform.cleaned_data['steps']
            first_name = request.user.first_name
            user = request.user.email
            s = Steps(steps=steps_data, submit_date=date.today(), first_name=first_name, user=user)
            s.save()
            return redirect('home')
    else:
        if request.user.is_authenticated:
            # Checks if the user has already entered a goal for the week. Redirects them otherwise.
            if Goals.objects.filter(first_name=request.user.first_name) and Goals.objects.filter(submit_date__range=(this_monday, next_monday)):
                stepsform = StepsForm()
                form = None
        else:
            form = GoalsForm()
            stepsform = StepsForm()

    context = {
        'form': form,
        'stepsform': stepsform,
    }

    return render(request, 'steps/steps.html', context)
