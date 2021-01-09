from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=128)
    company_search_url = models.URLField()
    company_logo = models.TextField()
    function_name = models.TextField()


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=128)
    description_url = models.URLField()

    @classmethod
    def push_data_api(cls, company_name_api, title_list, url_list):
        combined = zip(title_list, url_list)
        combined_list = list(combined)
        title_list, url_list = zip(*combined_list)

        for job_title, description_url in combined_list:
            company_job = Company.objects.get(company_name=company_name_api)
            cls(company=company_job, job_title=job_title, description_url=description_url).save()

    @classmethod
    def get(cls):
        return cls.company_name

# Create your models here.
