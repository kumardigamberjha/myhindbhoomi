# Generated by Django 3.1.7 on 2021-06-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_flight',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
