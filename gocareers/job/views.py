from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from . import models as job_models
from . import serializers as job_serializers


class GetSpecificJob(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = job_serializers.GetSpecificJobSerializer
    def get_queryset(self):
        return job_models.Job.objects.filter(pk=self.kwargs['job_id'])
