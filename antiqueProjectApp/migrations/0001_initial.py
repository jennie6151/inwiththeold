# Generated by Django 2.2.3 on 2019-08-05 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='antiqueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an antique or collectable type (e.g. Pottery vase)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=120)),
                ('date_of_creation', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['creator_name'],
            },
        ),
        migrations.CreateModel(
            name='Antique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a description of the antique', max_length=1000)),
                ('antiqueType', models.ManyToManyField(help_text='Select a type for this antique', to='antiqueProjectApp.antiqueType')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='antiqueProjectApp.Creator')),
            ],
        ),
    ]
