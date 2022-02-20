from rest_framework import serializers

from . import models as job_models


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_models.Job
        fields = '__all__'
