from django.contrib import admin

from .models import (
    Job
)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'company_name', 'get_expected_salary', 'location',
        'min_year_of_experience', 'college_grads_batch', 'job_type', 'degree',
        'roles_and_responsibilities', 'skills', 'true_job_link', 'id'
    )
    search_fields = (
        'title', 'company_name', 'expected_salary', 'location',
        'min_year_of_experience', 'college_grads_batch', 'job_type', 'degree',
        'roles_and_responsibilities', 'skills', 'true_job_link', 'id'
    )

    def get_expected_salary(self, obj):
        return f'{obj.expected_salary} LPA'
    get_expected_salary.short_description = 'expected salary'
