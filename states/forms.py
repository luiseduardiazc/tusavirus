from django import forms
from .models import State


class ReportForm(forms.Form):
    '''
    Report form.
    '''
    state = forms.ModelChoiceField(
        queryset=State.objects.all().order_by('name'))
    sick_people = forms.CharField(label='Sick People', max_length=200, required = True)

class GetReportForm(forms.Form):
    '''
    Get Report.
    '''
    get_report = forms.BooleanField()
