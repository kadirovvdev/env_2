# Generated by Django 5.0.4 on 2024-05-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soccers',
            name='number',
            field=models.IntegerField(),
        ),
    ]