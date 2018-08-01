# Generated by Django 2.0.7 on 2018-07-31 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0010_auto_20180730_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart_item',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Shopping_cart',
        ),
    ]
