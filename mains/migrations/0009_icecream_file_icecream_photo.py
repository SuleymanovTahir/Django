# Generated by Django 4.2 on 2024-02-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0008_alter_icecream_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='file',
            field=models.FileField(null=True, upload_to='fileForm'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='photo',
            field=models.ImageField(null=True, upload_to='photoForm'),
        ),
    ]
