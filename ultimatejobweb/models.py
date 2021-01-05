from django.db import models


class company(models.Model):
    company_name = models.CharField(max_length=128)
    company_search_url = models.URLField()
    company_logo = models.TextField()
    function_name = models.TextField()


class job(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=128)
    description_url = models.URLField()

    def push_data_api(company_name_api, title_list, url_list):
        combined = zip(title_list, url_list)
        combined_list = list(combined)
        title_list, url_list = zip(*combined_list)

        for job_title, description_url in combined_list:
            company_job = company.objects.get(company_name=company_name_api)
            job(company=company_job, job_title=job_title, description_url=description_url).save()

# Create your models here.
