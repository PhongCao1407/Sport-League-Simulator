# Generated by Django 4.1.3 on 2022-11-25 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sportleagues", "0002_alter_sport_table"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Sport",
        ),
    ]
