# Django Imports
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db.models import Sum

# Build Imports
from states.models import Report
from utilities.utility_number import ToNumber
from states.forms import ReportForm, GetReportForm


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        form = ReportForm()
        get_form = GetReportForm()
        report = dict()
        total = int()
        submitbutton = request.GET.get('get_data')
        if submitbutton:
            report, total = self.create_report()

        args = {
            'form': form, 'get_form': get_form,  'title': 'States', 'report': report, 'total': total
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = ReportForm(request.POST)
        get_form = GetReportForm()
        if form.is_valid():
            data = form.cleaned_data
            sick_people = self.validade_sick_people(data['sick_people'])

            if sick_people == -1:
                message = "Invalid Inpud"
            else:
                Report.objects.update_or_create(
                    state=data['state'], victims=sick_people)
                message = "Saved! {} Sick people for {}".format(
                    sick_people, data['state'].name)
                form = ReportForm()

        args = {
            'form': form, 'get_form': get_form, 'message': message
        }

        return render(request, self.template_name, args)

    def validade_sick_people(self, sick_people):
        '''
        validate
        '''
        if sick_people.isdigit():
            return int(sick_people)

        to_num = ToNumber()
        sick_people = to_num.words_to_number(sick_people)
        return sick_people

    def create_report(self):
        '''
        <QuerySet [{'state__name': 'Antioquia', 'victims__sum': 48}]>
        '''
        report = Report.objects.values('state__name').annotate(Sum('victims'))
        total = Report.objects.all().aggregate(Sum('victims'))['victims__sum']
        return report, total
