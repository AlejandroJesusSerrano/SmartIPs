# Generated by Django 4.1.3 on 2022-11-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartipnav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='device',
            field=models.CharField(default=False, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='internet',
            field=models.BooleanField(default=False),
        ),
    ]