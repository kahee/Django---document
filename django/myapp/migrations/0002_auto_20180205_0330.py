# Generated by Django 2.0.2 on 2018-02-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='instrument',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
