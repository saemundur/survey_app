from django.contrib import admin
from single_instance_model.admin import SingleInstanceModelAdmin
from .models import EmployeeStatistics, OrganizationInformation, DescriptionLable, StatisticsLable

# Register your models here.

admin.site.register(EmployeeStatistics)
admin.site.register(OrganizationInformation)

@admin.register(DescriptionLable)
class DescriptionLableAdmin(SingleInstanceModelAdmin):
    pass

@admin.register(StatisticsLable)
class StatisticsLableAdmin(SingleInstanceModelAdmin):
    pass