# Generated by Django 4.2.4 on 2023-08-21 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfollows",
            name="lecteur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollows",
            name="lecteur_suivi",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
