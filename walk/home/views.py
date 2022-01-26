from datetime import date, timedelta
from django.shortcuts import render
from django.db.models import F, Sum
from steps.models import Target, TotalSteps

from django.contrib.auth.models import User
<<<<<<< HEAD

import operator
=======
>>>>>>> refs/remotes/origin/main


# Create your views here.
def index(request):
    """ creates the home page view """

    today = date.today()
    last_week = today - timedelta(days=7)
    monday_last = last_week - timedelta(days=(last_week.isocalendar()[2] - 1))
    this_monday = monday_last + timedelta(days=7)
    next_monday = this_monday + timedelta(days=7)

<<<<<<< HEAD
    week = Target.objects.filter(
                                        goal_submitted__range=(
                                            last_week, today)
                                        ).order_by(F('steps').desc())

    users = User.objects.all()

    week_leader = {}

    for x in users:
        keys = [x.first_name]
        total = week.filter(user=x)
        leader = total.aggregate(Sum("steps"))
        values = [leader["steps__sum"]]
        for i in range(len(keys)):
            week_leader[keys[i]] = values[i]

    week_leader = dict(sorted(week_leader.items(),
                              key=operator.itemgetter(1),
                              reverse=True))

    leaderboard = {}

    for x in users:
        keys = [x.first_name]
        total = Target.objects.filter(user=x)
        leader = total.aggregate(Sum("steps"))
        values = [leader["steps__sum"]]
        for i in range(len(keys)):
            leaderboard[keys[i]] = values[i]

    leaderboard = dict(sorted(leaderboard.items(),
                              key=operator.itemgetter(1),
                              reverse=True))

    # REDUNDANT AS LEADERBOARD HANDLED IN VIEW ABOVE
    # for x in users:
    #     total = Target.objects.filter(user=x)
    #     if TotalSteps.objects.filter(user=x):
    #         updateUser = TotalSteps.objects.get(user=x)
    #         leader = total.aggregate(Sum('steps'))
    #         new_steps = leader['steps__sum']
    #         updateUser.steps = new_steps
    #         updateUser.save()
    #     else:
    #         leader = total.aggregate(Sum('steps'))
    #         TotalSteps.objects.create(
    #             user=x,
    #             first_name=x.first_name,
    #             steps=leader['steps__sum']
    #             )

    # leaderboard = TotalSteps.objects.all().order_by(F('steps').desc())
=======
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
>>>>>>> refs/remotes/origin/main

    context = {
        'week_leader': week_leader,
        'leaderboard': leaderboard,
    }

    return render(request, 'home/index.html', context)
