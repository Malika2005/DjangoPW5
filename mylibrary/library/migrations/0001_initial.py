# Generated by Django 4.2.2 on 2023-06-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('publish_year', models.IntegerField()),
                ('colour', models.CharField(max_length=30)),
                ('mileage', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
