# Generated by Django 3.1.5 on 2021-01-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]
