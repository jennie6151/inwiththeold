# Generated by Django 2.2.4 on 2019-08-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0018_auto_20190820_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antique',
            name='AntiqueImage',
            field=models.FilePathField(blank=True, null=True, path='/img'),
        ),
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]