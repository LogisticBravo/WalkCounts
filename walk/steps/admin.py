from django.contrib import admin
from .models import Goals, Target
# Register your models here.


class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'goals',
        'submit_date',
        'first_name',
        'user',
    )


class TargetAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'goal',
        'goal_submitted',
        'steps',
    )


admin.site.register(Goals, GoalsAdmin)
admin.site.register(Target, TargetAdmin)
