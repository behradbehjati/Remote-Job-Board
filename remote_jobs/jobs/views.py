from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from scripts.flexjobs_script import flexjobs_script
from scripts.virtualvocations_script import virtualvocations_script
from scripts.weworkremotely_script import weworkremotely_script
from .serializers import JobSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics


class Pagination(PageNumberPagination):
    page_size = 8

class JobApiView(generics.ListAPIView):
    pagination_class=Pagination



    def get(self,request):
        search= self.request.query_params.get('field', None)
        flexjobs=flexjobs_script(search)
        virtualvocations=virtualvocations_script(search)
        weworkremotely=weworkremotely_script(search)
        combined_jobs = {}
        combined_jobs.update(flexjobs)
        combined_jobs.update(virtualvocations)
        combined_jobs.update(weworkremotely)
        page = self.paginate_queryset(list(combined_jobs.values()))
        ser_data=JobSerializer(page,many=True)


        return self.get_paginated_response(ser_data.data)

