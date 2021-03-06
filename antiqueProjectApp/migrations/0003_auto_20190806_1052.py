# Generated by Django 2.2.3 on 2019-08-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueProjectApp', '0002_auto_20190805_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'ordering': ['CreatorName']},
        ),
        migrations.RenameField(
            model_name='antique',
            old_name='creator',
            new_name='Creator',
        ),
        migrations.RenameField(
            model_name='antique',
            old_name='summary',
            new_name='Summary',
        ),
        migrations.RenameField(
            model_name='antique',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='creator',
            old_name='creator_name',
            new_name='CreatorName',
        ),
        migrations.RemoveField(
            model_name='creator',
            name='date_of_creation',
        ),
        migrations.AddField(
            model_name='antique',
            name='DateOfCreation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='antique',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='antique',
            name='AntiqueType',
            field=models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.AntiqueType'),
        ),
    ]
