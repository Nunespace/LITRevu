# Generated by Django 4.2.4 on 2023-08-28 21:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0005_userfollows_followed_user_search_alter_review_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userfollows",
            name="followed_user_search",
        ),
    ]