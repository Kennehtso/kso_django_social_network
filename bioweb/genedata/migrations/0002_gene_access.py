# Generated by Django 4.2.1 on 2023-06-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='access',
            field=models.IntegerField(default=0),
        ),
    ]