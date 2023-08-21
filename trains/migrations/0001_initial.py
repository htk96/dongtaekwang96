# Generated by Django 4.2.4 on 2023-08-21 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Train",
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
                ("train_word_count", models.IntegerField()),
                ("train_seconds", models.IntegerField()),
                ("train_repeat", models.IntegerField()),
                ("train_tts_play", models.BooleanField()),
                ("exam_word_count", models.IntegerField()),
                ("exam_seconds", models.IntegerField()),
                ("exam_tts_play", models.BooleanField()),
                ("exam_difficulty", models.IntegerField()),
                ("update_date", models.DateTimeField(auto_now_add=True)),
                (
                    "id_user",
                    models.ForeignKey(
                        db_column="id_user",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="train_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
