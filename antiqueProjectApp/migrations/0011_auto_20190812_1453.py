# Generated by Django 2.2.3 on 2019-08-12 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0010_auto_20190812_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiquesale',
            name='saleDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]
