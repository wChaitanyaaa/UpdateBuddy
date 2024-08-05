# Generated by Django 5.0.7 on 2024-08-01 08:27

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_learnings_learning_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnings',
            name='learning_detail',
            field=models.TextField(default='Enter learning details'),
        ),
        migrations.AddField(
            model_name='learnings',
            name='links',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='learnings',
            name='subject',
            field=models.CharField(choices=[('DSA', 'DSA'), ('Web development', 'Web development'), ('App development', 'App development'), ('DBMS', 'DBMS'), ('android development', 'android development'), ('Data Science', 'Data Science'), ('OS', 'OS'), ('Networking', 'Networking'), ('Apptitude', 'Apptitude')], default='select subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='learnings',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='learnings',
            name='hours_learned',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.5)]),
        ),
    ]
