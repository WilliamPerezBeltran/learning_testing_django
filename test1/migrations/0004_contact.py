# Generated by Django 2.2 on 2020-07-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test1", "0003_event"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=400)),
            ],
        ),
    ]
