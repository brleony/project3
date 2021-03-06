# Generated by Django 2.0.7 on 2018-07-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Type of salad?')),
                ('large', models.BooleanField(verbose_name='Is it a large dinner platter?')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Mozzarella, meatballs or chicken?')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sicilian', models.BooleanField(verbose_name='Is it a Sicilian pizza?')),
                ('num_toppings', models.IntegerField(verbose_name='Number of toppings')),
                ('large', models.BooleanField(verbose_name='Is it a large pizza?')),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Type of salad?')),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='What is on the sub?')),
                ('large', models.BooleanField(verbose_name='Is it a large sub?')),
                ('extra_cheese', models.BooleanField(verbose_name='Is extra cheese added?')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Toppings'),
        ),
    ]
