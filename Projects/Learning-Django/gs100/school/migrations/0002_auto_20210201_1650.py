# Generated by Django 3.1.5 on 2021-02-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
