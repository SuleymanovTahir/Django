# Generated by Django 5.0.1 on 2024-02-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0002_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
