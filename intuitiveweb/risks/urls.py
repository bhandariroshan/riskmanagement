from django.conf.urls import url
from .api import ListRiskTypeView, ListAllRiskTypeView, ListAllRiskFieldView, ListRiskFieldView

urlpatterns = [
    url(
        regex=r'^types/$',
        view=ListAllRiskTypeView.as_view(),
        name='all_risk_types'
    ),
    url(
        regex=r'^types/(?P<id>[-\w]+)/$',
        view=ListRiskTypeView.as_view(),
        name='singlerisktype'
    ),
    url(
        regex=r'^fields/$',
        view=ListAllRiskFieldView.as_view(),
        name='allrisk'
    ),
    url(
        regex=r'^fields/(?P<id>[-\w]+)/$',
        view=ListRiskFieldView.as_view(),
        name='singlerisk'
    ),
]
