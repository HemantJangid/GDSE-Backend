# Generated by Django 3.1.7 on 2021-03-31 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210331_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcontent',
            name='info_page_metrics_2',
        ),
    ]
