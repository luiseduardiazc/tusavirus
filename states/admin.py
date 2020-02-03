from django.contrib import admin

from .models import State, Report


@admin.register(State)
class AdminState(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Report)
class AdminReport(admin.ModelAdmin):
    list_display = ('id', 'state', 'victims')
