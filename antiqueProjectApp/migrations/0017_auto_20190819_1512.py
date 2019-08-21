# Generated by Django 2.2.4 on 2019-08-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0016_auto_20190816_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiquesale',
            name='stripeId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]