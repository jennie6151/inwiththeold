# Generated by Django 2.2.3 on 2019-08-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0013_auto_20190814_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]
