from datetime import date, timedelta
from django.shortcuts import render
from django.db.models import F, Sum
from steps.models import Target, TotalSteps

from django.contrib.auth.models import User


# Create your views here.
def index(request):
    """ creates the home page view """

    today = date.today()
    last_week = today - timedelta(days=7)
    monday_last = last_week - timedelta(days=(last_week.isocalendar()[2] - 1))
    this_monday = monday_last + timedelta(days=7)
    next_monday = this_monday + timedelta(days=7)

    week_leader = Target.objects.filter(goal_submitted__range=(last_week, today)).order_by(F('steps').desc())

    users = User.objects.all()

    for x in users:
        total = Target.objects.filter(user=x)
        if TotalSteps.objects.filter(user=x):
            updateUser = TotalSteps.objects.get(user=x)
            leader = total.aggregate(Sum('steps'))
            new_steps = leader['steps__sum']
            updateUser.steps = new_steps
            updateUser.save()
        else:
            leader = total.aggregate(Sum('steps'))
            TotalSteps.objects.create(
                user=x,
                first_name=x.first_name,
                steps=leader['steps__sum']
                )

    leaderboard = TotalSteps.objects.all().order_by(F('steps').desc())

    context = {
        'week_leader': week_leader,
        'leaderboard': leaderboard,
    }

    return render(request, 'home/index.html', context)
