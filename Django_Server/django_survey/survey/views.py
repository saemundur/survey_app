from .models import EmployeeStatistics, OrganizationInformation, DescriptionLable, StatisticsLable
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json


def index(request):
    training_information = OrganizationInformation.objects.all()

    survey_information = json.dumps(
        [[t.employee_statistics.id, t.employee_statistics.trained_employee_count, t.training_description] for t in training_information])

    return JsonResponse(survey_information, safe=False)


def lables(request):
    training_lable = StatisticsLable.objects.get(pk=1)
    description_lable = DescriptionLable.objects.get(pk=1)

    lables = json.dumps(
        [training_lable.text, description_lable.text])

    return JsonResponse(lables, safe=False)


@api_view(('POST',))
@csrf_exempt
def submit(request):
    json_request = json.loads(request.body.decode('utf-8'))

    new_statistic = EmployeeStatistics(
        trained_employee_count=json_request['count'])
    new_statistic.save()

    new_information = OrganizationInformation(
        training_description=json_request['describtion'], employee_statistics=new_statistic)
    new_information.save()

    return Response(status=status.HTTP_201_CREATED)