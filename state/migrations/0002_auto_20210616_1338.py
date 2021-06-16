# Generated by Django 3.2.4 on 2021-06-16 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_population', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('zero_to_six_total_population', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('Total_literate', models.CharField(choices=[('Male literate', 'Male literate'), ('Female literate', 'Female literate')], max_length=100)),
                ('sex_ratio', models.CharField(max_length=100)),
                ('child_sex_ratio', models.CharField(max_length=100)),
                ('literate_rate_over_seven', models.CharField(choices=[('Male Literacy rate over Age 7', 'Male Literacy rate over Age 7'), ('Female Literacy rate over Age 7', 'Female Literacy rate over Age 7')], max_length=100)),
                ('total_graduate', models.CharField(choices=[('Male Graduates ', 'Male Graduates '), ('Female Graduates ', 'Female Graduates ')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='total_population',
        ),
        migrations.AddField(
            model_name='state',
            name='location',
            field=models.CharField(choices=[('Lag', 'Lag'), ('Log', 'Log')], default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='state_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(choices=[('Lag', 'Lag'), ('Log', 'Log')], max_length=100)),
                ('Total_population', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.population')),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='Total_population',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='state.population'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='city_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='state.city', unique=True),
        ),
    ]
