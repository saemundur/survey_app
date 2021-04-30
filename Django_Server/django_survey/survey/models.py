from django.db import models
from single_instance_model.models import SingleInstanceModel

# Input should be an INTEGER/NUMBER stored in a table called EmployeeStatistics,
# the attribute name could be "trained_employee_count"


class EmployeeStatistics(models.Model):
    trained_employee_count = models.IntegerField()

    def __str__(self):
        return str(self.trained_employee_count)


# Input should be TEXT stored in a table called OrganizationInformation,
# the attribute name could be "training_description"

class OrganizationInformation(models.Model):
    employee_statistics = models.OneToOneField(
        EmployeeStatistics, on_delete=models.CASCADE, primary_key=True)

    training_description = models.CharField(max_length=500)

    def __str__(self):
        return self.training_description


class StatisticsLable(models.Model, SingleInstanceModel):
    text = models.TextField(max_length=2000)


class DescriptionLable(models.Model, SingleInstanceModel):
    text = models.TextField(max_length=2000)