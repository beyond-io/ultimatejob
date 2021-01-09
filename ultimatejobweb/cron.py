import os
import tests.API_FB as fb
from ultimatejobweb.models import Job
import time


def my_scheduled_job():
    os.system('echo hello >> /vagrant/cron.out')
    Job.delete_data()
    time.sleep(3)
    Job.push_data_api("Facebook", fb.extract_jobs_title(fb.create_soup(fb.create_req())),
                      fb.extract_jobs_url(fb.create_soup(fb.create_req())))
