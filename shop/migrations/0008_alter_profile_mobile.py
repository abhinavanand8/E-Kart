# Generated by Django 4.0.4 on 2022-06-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
