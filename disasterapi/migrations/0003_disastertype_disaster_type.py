# Generated by Django 4.1.3 on 2022-11-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("disasterapi", "0002_remove_disaster_comment_disaster_geom"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisasterType",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name="disaster",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="disasterapi.disastertype",
            ),
        ),
    ]