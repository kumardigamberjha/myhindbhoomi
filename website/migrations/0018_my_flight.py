# Generated by Django 3.1.7 on 2021-06-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flight_name', models.CharField(default='', max_length=100)),
                ('Flight_No', models.IntegerField()),
                ('Source_Station_Name', models.CharField(max_length=300)),
                ('Destination_Station_Name', models.CharField(max_length=300)),
                ('days', models.CharField(max_length=50)),
                ('Economy', models.IntegerField(blank=True, default=0, null=True)),
                ('Bussiness', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
