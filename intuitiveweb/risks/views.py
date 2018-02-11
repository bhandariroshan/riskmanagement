from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class ShowRisks(View):
    """ View to enter marks for annual activities"""

    template_name = 'risks/home.html'
    url_name = 'risks:all_risk_types'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['return']:
            return render(
                request, self.template_name, context)
        else:
            return HttpResponse(context['return_message'])

    def get_context_data(self, **kwargs):
        context = {}
        context['return'] = True
        id = self.kwargs.get('id')
        return context


