# Generated by Django 2.0.2 on 2018-02-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_block', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user',),
        ),
    ]
