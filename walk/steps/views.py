from datetime import date, timedelta
from django.shortcuts import render, redirect

from .forms import GoalsForm, StepsForm
from .models import Target, DailySteps


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
    user_target = current_target.filter(goal_submitted__range=(this_monday, next_monday))

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GoalsForm(request.POST)
        stepsform = StepsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            goals = form.cleaned_data['goals']

            new_target = Target.objects.create(user=user)

            if new_target.goal == 0:
                new_target.goal = goals
                new_target.first_name = user.first_name
                new_target.goal_submitted = date.today()
                new_target.save()
            else:
                new_target.goal = goals
                new_target.first_name = user.first_name
                new_target.goal_submitted = date.today()
                new_target.save()

            new_target.save()
            return redirect('home')

        if stepsform.is_valid():
            steps_data = stepsform.cleaned_data['steps']

            new_steps = DailySteps()

            new_steps = DailySteps.objects.create(
                user=user,
                steps=steps_data,
                date=date.today()
            )

            new_steps.save()

            steps_total = current_target.get(goal_submitted__range=(this_monday, next_monday))
            steps_total.steps += steps_data
            steps_total.save()

            return redirect('home')
    else:
        if request.user.is_authenticated:
            # Checks if the user has already entered a goal for the week. Removes the form if so and displays their current goal.
            if current_target and Target.objects.filter(goal_submitted__range=(this_monday, next_monday)):

                new_target = current_target.filter(goal_submitted__range=(this_monday, next_monday))

                if not new_target:
                    form = GoalsForm()
                else:
                    stepsform = StepsForm()
                    form = None
        else:
            form = GoalsForm()
            stepsform = StepsForm()

    context = {
        'form': form,
        'stepsform': stepsform,
        'current_target': current_target,
        'user_target': user_target
    }

    return render(request, 'steps/steps.html', context)
