# Generated by Django 4.0.4 on 2022-05-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_orders_orderupdate_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=30000),
        ),
    ]
