# Generated by Django 2.0.2 on 2018-02-06 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_auto_20180205_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_posts', to='many_to_many.Post'),
        ),
    ]
