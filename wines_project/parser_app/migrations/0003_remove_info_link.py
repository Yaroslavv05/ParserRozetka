# Generated by Django 4.2.2 on 2023-06-27 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0002_alter_links_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='link',
        ),
    ]
