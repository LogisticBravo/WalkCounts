from datetime import date, timedelta
from django.shortcuts import render, redirect

from .forms import GoalsForm, StepsForm
from .models import Target


# Create your views here.
def steps(request):
    """ creates the steps target page view """

    user = request.user

    today = date.today()
    last_week = today - timedelta(days=7)
    monday_last = last_week - timedelta(days=(last_week.isocalendar()[2] - 1))
    this_monday = monday_last + timedelta(days=7)
    next_monday = this_monday + timedelta(days=7)

    form = GoalsForm()
    stepsform = StepsForm()

    current_target = Target()
    current_target = Target.objects.filter(user=user)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GoalsForm(request.POST)
        stepsform = StepsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            goals = form.cleaned_data['goals']

            new_target = Target.objects.get(user=user)

            if new_target.goal == 0:
                new_target.goal = goals
                new_target.goal_submitted = date.today()
                new_target.save()
            else:
                new_target.goal += goals
                new_target.goal_submitted = date.today()
                new_target.save()

            new_target.save()
            return redirect('home')

        if stepsform.is_valid():
            steps_data = stepsform.cleaned_data['steps']

            new_steps = Target.objects.get(user=user)

            if new_steps.steps == 0:
                new_steps.steps = steps_data
                new_steps.save()
            else:
                new_steps.steps += steps_data
                new_steps.save()

            return redirect('home')
    else:
        if request.user.is_authenticated:
            # Checks if the user has already entered a goal for the week. Redirects them otherwise.
            if current_target and Target.objects.filter(goal_submitted__range=(this_monday, next_monday)):
                stepsform = StepsForm()
                form = None
        else:
            form = GoalsForm()
            stepsform = StepsForm()

    context = {
        'form': form,
        'stepsform': stepsform,
        'current_target': current_target
    }

    return render(request, 'steps/steps.html', context)
