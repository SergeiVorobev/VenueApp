# Generated by Django 3.2 on 2021-05-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventuser',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
    ]
