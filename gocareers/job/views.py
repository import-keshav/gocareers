from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer

from . import models as job_models
from . import serializers as job_serializers


class GetAllJobsPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 9


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):        
        return request.GET.getlist('search_fields', [])


class GetJob(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = job_serializers.JobSerializer
    pagination_class = GetAllJobsPagination
    filter_backends = (DynamicSearchFilter,)

    def get_queryset(self):
        return job_models.Job.objects.all().order_by('-date_posted')


class GetSpecificJob(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = job_serializers.JobSerializer
    def get_queryset(self):
        return job_models.Job.objects.filter(pk=self.kwargs['job_id'])
