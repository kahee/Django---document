# Generated by Django 2.0.2 on 2018-02-06 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0007_auto_20180206_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facebookuser',
            options={'verbose_name_plural': 'self - FacebookUser'},
        ),
        migrations.AlterModelOptions(
            name='instagramuser',
            options={'verbose_name_plural': 'symmetrical- InstagramUser'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'Basic - Pizzas'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'intermediate - Post'},
        ),
        migrations.AlterModelOptions(
            name='postlike',
            options={'verbose_name_plural': 'intermediate - PostLike'},
        ),
        migrations.AlterModelOptions(
            name='relation',
            options={'verbose_name_plural': 'symmetrical_intermediate - Relation'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Basic - Topping'},
        ),
        migrations.AlterModelOptions(
            name='twitteruser',
            options={'verbose_name_plural': 'symmetrical_intermediate - TwitterUser'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'intermediate - User'},
        ),
    ]
