# Generated by Django 4.2.4 on 2023-08-19 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("words", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exam",
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
                ("in_word", models.CharField(max_length=50)),
                ("exam_right", models.BooleanField()),
                ("exam_point", models.DecimalField(decimal_places=2, max_digits=3)),
                ("reg_date", models.DateTimeField(auto_now_add=True)),
                (
                    "id_user",
                    models.ForeignKey(
                        db_column="id_user",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "id_word",
                    models.ForeignKey(
                        db_column="id_word",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="word",
                        to="words.word",
                    ),
                ),
            ],
        ),
    ]