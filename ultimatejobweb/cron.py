import os
import sys

def my_scheduled_job():
   os.system('echo hello >> /vagrant/cron.out')
