# Generated by Django 4.2.2 on 2023-06-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField()),
                ('reviews', models.IntegerField()),
                ('characteristic1', models.CharField(max_length=100)),
                ('characteristic2', models.CharField(max_length=100)),
                ('characteristic3', models.CharField(max_length=100)),
                ('characteristic4', models.CharField(max_length=100)),
                ('characteristic5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default='New')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('status', models.BooleanField(default='New')),
            ],
        ),
    ]
