from .models import RiskType, RiskField
from rest_framework import routers, serializers, viewsets


class RiskSerializer(serializers.ModelSerializer):
    risk_id = serializers.CharField(
        source='risk_type.id',
        allow_blank=True,
        required=False
    )
    risk_name = serializers.CharField(
        source='risk_type.name',
        allow_blank=True,
        required=False
    )

    class Meta:
        model = RiskField
        fields = (
            'id',
            'risk_id',
            'risk_name',
            'risk_field_name',
            'risk_field_data_type'
        )

class RiskTypeSerializer(serializers.ModelSerializer):
    riskfields = RiskSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType

        fields = (
            'id',
            'name',
            'riskfields'
        )
