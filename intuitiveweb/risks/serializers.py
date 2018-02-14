from .models import RiskType, RiskField, RiskFieldChoices
from rest_framework import routers, serializers, viewsets


class RiskFieldChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFieldChoices

        fields = (
            'risk_field_id',
            'choice'
        )

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

    risk_field_choices = serializers.SerializerMethodField('get_choices')

    def get_choices(self, riskfield):
        """

        :param riskfield:
        :return:
        """

        qs = RiskFieldChoices.objects.filter(risk_field_id=riskfield)
        serializer = RiskFieldChoicesSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = RiskField
        fields = (
            'id',
            'risk_id',
            'risk_name',
            'risk_field_name',
            'risk_field_choices',
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
