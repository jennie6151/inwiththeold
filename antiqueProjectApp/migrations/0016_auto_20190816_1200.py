# Generated by Django 2.2.4 on 2019-08-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0015_auto_20190815_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]
