# Generated by Django 3.1.7 on 2021-03-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_productcontent_info_page_metrics_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='display_position',
            field=models.IntegerField(blank=True),
        ),
    ]
