# Generated by Django 3.2.4 on 2021-06-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_alter_population_zero_to_six_total_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population',
            name='literate_rate_over_seven',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='population',
            name='zero_to_six_total_population',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]
