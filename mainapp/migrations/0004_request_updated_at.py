# Generated by Django 2.0.7 on 2018-08-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180816_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]