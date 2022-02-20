from django.urls import path

from . import views

urlpatterns = [
	path('get-job/<int:job_id>', views.GetSpecificJob.as_view()),
]