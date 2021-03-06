# Generated by Django 2.2.3 on 2019-08-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0008_auto_20190811_1537'),
    ]

    operations = [
        migrations.AddField(
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
