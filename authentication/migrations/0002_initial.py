# Generated by Django 4.2.4 on 2023-08-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="users_followed",
            field=models.ManyToManyField(to="review.userfollows"),
        ),
    ]