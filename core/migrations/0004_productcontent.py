# Generated by Django 3.1.7 on 2021-03-31 10:47

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_main_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_page_title', models.CharField(blank=True, max_length=255, null=True)),
                ('landing_page_image', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('brochure_link', models.CharField(blank=True, max_length=255, null=True)),
                ('info_page_content_1', models.TextField(blank=True, null=True)),
                ('info_page_content_2', models.TextField(blank=True, null=True)),
                ('info_page_metrics_1', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=core.models.get_default_list, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'db_table': 'product_content',
            },
        ),
    ]
