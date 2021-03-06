# Generated by Django 4.0.3 on 2022-03-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Laptop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("SURFACEPRO", "Surface Pro"),
                            ("MACBOOK", "MacBook"),
                            ("THINKPAD", "Thinkpad"),
                        ],
                        max_length=100,
                    ),
                ),
                ("owner", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "Device is available to be assigned"),
                            ("ASSIGNED", "Device is assigned to a staff member"),
                            (
                                "SETUP_REQUIRED",
                                "This device needs setting up before it can be assigned",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mobile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("ANDROID", "Android"),
                            ("IPHONE", "iPhone"),
                            ("SAMSUNG", "Samsung"),
                        ],
                        max_length=100,
                    ),
                ),
                ("owner", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "Device is available to be assigned"),
                            ("ASSIGNED", "Device is assigned to a staff member"),
                            (
                                "SETUP_REQUIRED",
                                "This device needs setting up before it can be assigned",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
