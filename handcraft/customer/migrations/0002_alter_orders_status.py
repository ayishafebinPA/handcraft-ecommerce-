# Generated by Django 4.2.4 on 2023-08-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('deliverd', 'delivered'), ('order placed', 'order placed'), ('cancel', 'cancel'), ('out for delivery', 'out for delivery'), ('shipped', 'shipped')], default='order placed', max_length=100),
        ),
    ]