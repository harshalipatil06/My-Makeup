# Generated by Django 4.1.2 on 2022-12-18 10:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('landmark', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=520)),
                ('pin', models.IntegerField()),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=1000)),
                ('dateOfOrder', models.DateTimeField(default=datetime.datetime.now)),
                ('details', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.userinfo')),
            ],
            options={
                'db_table': 'OrderMaster',
            },
        ),
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('price', models.FloatField(default=200)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.userinfo')),
            ],
            options={
                'db_table': 'MyOrder',
            },
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('prdt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
