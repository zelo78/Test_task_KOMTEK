from datetime import date, datetime

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from main.models import Resource, ResourceIdentifier
from main.serializers import ResourceSerializer


class ResourceList(generics.ListAPIView):
    """
    Список всех справочников в системе. Опциональная фильтрация по дате, на которую справочники должны быть актуальны.
    """
    # queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get_queryset(self):
        """
        Опциональная фильтрация по дате, на которую должны быть валидны справочники.
        """
        valid_date = self.request.query_params.get('date')
        if valid_date is not None:
            queryset = Resource.objects.filter(valid_from__lte=valid_date)
        else:
            queryset = Resource.objects.all()
        return queryset
