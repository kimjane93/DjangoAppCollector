# Generated by Django 3.1.5 on 2021-01-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_technologie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='built',
            field=models.CharField(choices=[('B', 'Built'), ('NB', 'Not Built')], default='Not Built', max_length=2),
        ),
    ]
