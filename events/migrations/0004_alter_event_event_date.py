# Generated by Django 3.2 on 2021-05-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210501_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='Event Date'),
        ),
    ]
