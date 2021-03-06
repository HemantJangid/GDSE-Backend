# Generated by Django 3.1.7 on 2021-04-05 15:43

import core.models
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210401_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.RenameField(
            model_name='productcontent',
            old_name='landing_page_title',
            new_name='landing_page_title1',
        ),
        migrations.AddField(
            model_name='productcontent',
            name='info_page_metrics_2',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=core.models.get_default_list, size=None),
        ),
        migrations.AddField(
            model_name='productcontent',
            name='landing_page_bg_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcontent',
            name='landing_page_title2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
