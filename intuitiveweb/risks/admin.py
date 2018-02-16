from django.contrib import admin
from .models import RiskType, RiskField, RiskFieldChoices
from django import forms

# Register your models here.
@admin.register(RiskFieldChoices)
class RiskFieldChoicesAdmin(admin.ModelAdmin):
    """ Admin class for RiskType Result."""
    # form = MyFieldChoiceForm
    list_display = (
        "id", "risk_field_id", "choice",
    )
    ordering = ("id",)

# class MyFieldChoiceForm(forms.ModelForm):
#     risk_field_id = CustomModelChoiceField(queryset=RiskField.objects.all())
#     class Meta:
#           model = RiskFieldChoices
#
# class CustomModelChoiceField(forms.ModelChoiceField):
#      def label_from_instance(self, obj):
#          return "%s %s" % (obj.risk_type.name, obj.last_name)

# Register your models here.
@admin.register(RiskType)
class RiskTypeAdmin(admin.ModelAdmin):
    """ Admin class for RiskType Result."""

    list_display = (
        "id", "name",
    )
    ordering = ("id",)

@admin.register(RiskField)
class RiskFieldAdmin(admin.ModelAdmin):
    """ Admin class for RiskField Result."""

    list_display = (
        "id", "risk_type", "risk_field_name", 'risk_field_data_type',
    )
    ordering = ("id",)
