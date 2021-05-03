# Generated by Django 3.2 on 2021-05-01 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='hone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('post_code', models.CharField(max_length=10, verbose_name='Post Code')),
                ('phone', models.CharField(max_length=15, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('ven_description', models.TextField(blank=True)),
                ('booking_rates', models.FloatField(default=1.0, verbose_name='Ranking (up to 9.9)')),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('flour_size', models.FloatField(default=1.0, verbose_name='Square (mxm)')),
                ('type', models.CharField(max_length=255, verbose_name='Type of Venue')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(auto_now_add=True, verbose_name='Event Date')),
                ('manager', models.CharField(max_length=50, verbose_name='Manager')),
                ('man_phone', models.CharField(max_length=15, verbose_name='Manager Phone')),
                ('eve_description', models.TextField(blank=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('attendees', models.ManyToManyField(blank=True, to='events.EventUser')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]