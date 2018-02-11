from .models import RiskField, RiskType
from .serializers import RiskSerializer, RiskTypeSerializer

from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ListAllRiskTypeView(ListAPIView):
    """API to get one object of RiskField model"""

    serializer_class = RiskTypeSerializer
    queryset = RiskType.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset

class ListRiskTypeView(RetrieveAPIView):
    """API to get one object of RiskField model"""

    serializer_class = RiskTypeSerializer
    queryset = RiskType.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        id = self.kwargs.get('id', None)
        obj = get_object_or_404(queryset,pk=id)
        return obj

class ListAllRiskFieldView(ListAPIView):
    """API to get one object of RiskField model"""

    serializer_class = RiskSerializer
    queryset = RiskField.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset

class ListRiskFieldView(RetrieveAPIView):
    """API to get one object of RiskField model"""

    serializer_class = RiskSerializer
    queryset = RiskField.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        id = self.kwargs.get('id', None)
        obj = get_object_or_404(queryset,pk=id)
        return obj


