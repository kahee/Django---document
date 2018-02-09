# Generated by Django 2.0.2 on 2018-02-08 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_foods', related_query_name='rel_food', to='rel.Person'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_fruits', related_query_name='rel_fruit', to='rel.Person'),
        ),
    ]
