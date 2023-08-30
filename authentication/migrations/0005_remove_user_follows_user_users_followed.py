# Generated by Django 4.2.4 on 2023-08-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0002_alter_userfollows_lecteur_and_more"),
        ("authentication", "0004_remove_user_users_followed_user_follows"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="follows",
        ),
        migrations.AddField(
            model_name="user",
            name="users_followed",
            field=models.ManyToManyField(
                blank=True, null=True, to="review.userfollows"
            ),
        ),
    ]
