# Generated by Django 3.1.7 on 2021-04-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
