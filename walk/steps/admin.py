from django.contrib import admin
from .models import Goals, Steps
# Register your models here.


class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'goals',
        'submit_date',
        'first_name',
        'user',
    )


class StepsAdmin(admin.ModelAdmin):
    list_display = (
        'steps',
        'submit_date',
        'first_name',
        'user',
    )


admin.site.register(Goals, GoalsAdmin)
admin.site.register(Steps, StepsAdmin)
