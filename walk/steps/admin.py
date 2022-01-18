from django.contrib import admin
from .models import Goals
# Register your models here.


class GoalsAdmin(admin.ModelAdmin):
    list_display = (
        'goals',
        'submit_date',
        'first_name',
    )


admin.site.register(Goals, GoalsAdmin)
