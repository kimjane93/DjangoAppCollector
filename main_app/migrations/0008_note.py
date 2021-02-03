# Generated by Django 3.1.5 on 2021-02-03 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210203_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.app')),
            ],
        ),
    ]
