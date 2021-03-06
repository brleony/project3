# Generated by Django 2.0.7 on 2018-07-30 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0009_auto_20180730_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(choices=[('SUB', 'Sub'), ('PAST', 'Pasta'), ('SALA', 'Salad'), ('DIPL', 'Dinner Plate'), ('SIPI', 'Sicilian Pizza'), ('REPI', 'Regular Pizza')], max_length=4, verbose_name='What kind of item is this?')),
                ('choice', models.CharField(blank=True, max_length=64, verbose_name='What flavor is it?')),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('L', 'Large')], max_length=2, verbose_name='What size item is this?')),
                ('num_toppings', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='What does it cost?')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart_item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Shopping_cart'),
        ),
        migrations.AddField(
            model_name='cart_item',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
    ]
