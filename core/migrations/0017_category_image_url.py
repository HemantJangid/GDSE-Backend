# Generated by Django 3.1.7 on 2021-04-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_category_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
