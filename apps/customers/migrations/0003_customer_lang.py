# Generated by Django 3.2.19 on 2023-07-12 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('customers', '0002_auto_20230707_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lang',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.language'),
        ),
    ]