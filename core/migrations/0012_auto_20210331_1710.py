# Generated by Django 3.1.7 on 2021-03-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210331_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
