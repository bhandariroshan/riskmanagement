from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from intuitiveweb.risks.models import RiskType


class ShowRisks(View):
    """ View to enter marks for annual activities"""

    template_name = 'risks/home.html'
    url_name = 'risks:all_risk_types'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        risktypeid = context['risktypeid']

        if not risktypeid:
            try:
                risktypeid = RiskType.objects.filter()[0].id
            except:
                risktypeid = 1

        context['risktypeid'] = risktypeid

        if context['return']:
            return render(
                request, self.template_name, context)
        else:
            return HttpResponse(context['return_message'])

    def get_context_data(self, **kwargs):
        context = {}
        context['return'] = True
        risktypeid = self.kwargs.get('id', None)
        context['risktypeid'] = risktypeid
        return context


