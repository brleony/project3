# Generated by Django 2.0.7 on 2018-07-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180728_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='ordered_item',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='What does this topping cost?'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='topping',
            field=models.CharField(max_length=4),
        ),
    ]
