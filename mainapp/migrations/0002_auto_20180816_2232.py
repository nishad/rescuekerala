# Generated by Django 2.1 on 2018-08-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='requestee_phone',
            field=models.CharField(max_length=15, verbose_name='Requestee Phone - അപേക്ഷകന്\u200dറെ ഫോണ്\u200d നമ്പര്\u200d'),
        ),
    ]
