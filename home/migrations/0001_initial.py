# Generated by Django 5.1.4 on 2024-12-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(blank=True, max_length=1000, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("published", "published"), ("draft", "draft")],
                        default="draft",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]