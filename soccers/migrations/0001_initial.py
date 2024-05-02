# Generated by Django 5.0.4 on 2024-05-02 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Soccers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100)),
                ('number', models.IntegerField(max_length=100)),
                ('body', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='soccers/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccers.category')),
            ],
            options={
                'db_table': 'soccers',
            },
        ),
    ]