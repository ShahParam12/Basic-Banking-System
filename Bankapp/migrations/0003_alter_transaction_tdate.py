# Generated by Django 3.2.1 on 2021-07-04 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tdate',
            field=models.DateField(verbose_name=datetime.datetime(2021, 7, 5, 5, 27, 13, 586312)),
        ),
    ]
