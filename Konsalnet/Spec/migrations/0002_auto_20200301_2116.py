# Generated by Django 3.0.2 on 2020-03-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specramadd',
            name='Computer',
            field=models.CharField(default='Ass', max_length=100),
        ),
        migrations.AddField(
            model_name='specramadd',
            name='Ram',
            field=models.CharField(default='Ass', max_length=100),
        ),
    ]