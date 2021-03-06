# Generated by Django 3.1.7 on 2021-06-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_mytrains'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(default='', max_length=100)),
                ('source_number', models.IntegerField()),
                ('contact_name', models.CharField(default='', max_length=100)),
                ('contact_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('seat_number', models.CharField(default='', max_length=100)),
                ('total_ticket', models.IntegerField()),
            ],
        ),
    ]
