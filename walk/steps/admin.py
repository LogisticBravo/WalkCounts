from django.contrib import admin
from .models import Target, DailySteps
# Register your models here.


class TargetAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'goal',
        'goal_submitted',
        'steps',
    )

    ordering = ('user', 'goal_submitted')


class DailyStepsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'steps',
        'date'
    )

    ordering = ('user', 'date')


admin.site.register(DailySteps, DailyStepsAdmin)
admin.site.register(Target, TargetAdmin)
