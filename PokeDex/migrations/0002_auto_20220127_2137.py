# Generated by Django 2.2.5 on 2022-01-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeDex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
