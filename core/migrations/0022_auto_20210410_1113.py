# Generated by Django 3.1.7 on 2021-04-10 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='name',
        ),
    ]