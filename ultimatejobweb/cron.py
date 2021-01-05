import os


def my_scheduled_job():
    os.system('echo hello >> /vagrant/cron.out')
