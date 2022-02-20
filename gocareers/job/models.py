from django.db import models
from django.core.validators import MinValueValidator


JOB_TYPES = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Contract", "Contract"),
    ("Internship", "Internship"),
    ("Volunteer", "Volunteer"),
    ("Temporary", "Temporary")
)


class Job(models.Model):
    title = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500)
    expected_salary = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    min_year_of_experience = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    college_grads_batch = models.IntegerField(validators=[MinValueValidator(0)],  null=True, blank=True)
    job_type = models.TextField(choices=JOB_TYPES)
    degree = models.CharField(max_length=1000, null=True, blank=True)
    roles_and_responsibilities = models.TextField()
    skills = models.TextField()
    true_job_link = models.TextField()
    image = models.FileField(null=True, blank=True, upload_to="")
    date_posted = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Job'

    def __str__(self):
        return f'{self.company_name} | {self.title}'
