# Generated by Django 4.0.6 on 2022-07-15 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
