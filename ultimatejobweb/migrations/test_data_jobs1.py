from django.db import migrations, transaction
from django.db import models
from django.contrib.auth.models import User

class Migration(migrations.Migration):

    dependencies = [
     ('ultimatejobweb', '0002_auto_20201212_1919'),
    ]

    def generate_data(apps, schema_editor):
        from ultimatejobweb.models import Jobs
        def populate_data(Jobs, parent=None)
            for user in Jobs
            user1 = User.objects.create_user (username = 'omer', password = 'sisma1', email = 'omer@nomer.com')
            user2 = User.objects.create_user (username = 'rom', password = 'sisma1', email = 'rom@nomer.com')
        test_data = [
          ('user', 'Facebook', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/1672813472870915/'),
          ('user2', 'Facebook', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/712878282607325/'),
        ]

        with transaction.atomic():
            for id, user, CompanyName, JobTitle, ApplyURL in test_data:
                Jobs(id=id, user=user, CompanyName=CompanyName, JobTitle=JobTitle, ApplyURL=ApplyURL).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
