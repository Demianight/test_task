# Generated by Django 5.0.1 on 2024-01-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productamount',
            old_name='amount',
            new_name='weight',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_amount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
