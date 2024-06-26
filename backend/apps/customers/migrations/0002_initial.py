# Generated by Django 4.2.11 on 2024-04-12 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routines', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='goals',
            field=models.ManyToManyField(blank=True, to='routines.goal'),
        ),
        migrations.AddField(
            model_name='customer',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='routines.level'),
        ),
        migrations.AddField(
            model_name='customer',
            name='restrictions',
            field=models.ManyToManyField(blank=True, to='routines.restriction'),
        ),
        migrations.AddField(
            model_name='customer',
            name='routines',
            field=models.ManyToManyField(blank=True, through='routines.RoutineCustomers', to='routines.routine'),
        ),
        migrations.AddField(
            model_name='customer',
            name='trainings_preferences',
            field=models.ManyToManyField(blank=True, to='routines.training'),
        ),
    ]
