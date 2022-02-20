from django.urls import path

from . import views

urlpatterns = [
	path('get-jobs', views.GetJob.as_view()),
	path('get-job/<int:job_id>', views.GetSpecificJob.as_view()),
]