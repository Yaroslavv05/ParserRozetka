# Generated by Django 4.2.2 on 2023-06-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0003_remove_info_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='reviews',
            field=models.CharField(max_length=100),
        ),
    ]
