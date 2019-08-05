# Generated by Django 2.2.3 on 2019-08-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antique',
            name='antiqueType',
        ),
        migrations.AddField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]
