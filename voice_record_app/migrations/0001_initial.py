# Generated by Django 4.1.1 on 2023-08-09 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Domaine",
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
                ("nom", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Audio",
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
                ("audio", models.FileField(upload_to="audio_files/")),
                ("date", models.DateTimeField()),
                ("auteur", models.CharField(max_length=100)),
                (
                    "domaine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="voice_record_app.domaine",
                    ),
                ),
            ],
        ),
    ]
