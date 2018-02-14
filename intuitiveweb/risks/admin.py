from django.contrib import admin
from .models import RiskType, RiskField, RiskFieldChoices

# Register your models here.
@admin.register(RiskFieldChoices)
class RiskTypeAdmin(admin.ModelAdmin):
    """ Admin class for RiskType Result."""

    list_display = (
        "id", "risk_field_id", "choice",
    )
    ordering = ("id",)


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
