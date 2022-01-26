from django.db import models
from django.contrib.auth.models import User


class Target(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    goal = models.IntegerField(null=True)
    goal_submitted = models.DateTimeField('goal submitted', null=True)
    steps = models.IntegerField('Total Steps', null=True, default=0)

    def __str__(self):
        return f"{self.user}, {self.goal}, {self.steps}, {self.first_name}"


class DailySteps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(null=True, default=0)
    date = models.DateTimeField('Date', null=True)

    class Meta:
        verbose_name_plural = 'Daily Steps'

    def __str__(self):
        return f"{self.user}, {self.steps}"


class TotalSteps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    steps = models.IntegerField(null=True, default=0)

    class Meta:
        verbose_name_plural = 'Total Steps'

    def __str__(self):
        return f"{self.user}, {self.first_name}, {self.steps}"
