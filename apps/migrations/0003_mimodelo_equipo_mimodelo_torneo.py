# Generated by Django 5.1.7 on 2025-05-24 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_mimodelo_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='mimodelo',
            name='equipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mimodelo',
            name='torneo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
