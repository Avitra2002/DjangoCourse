# Generated by Django 4.2 on 2024-09-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://archive.org/download/placeholder-image/placeholder-image.jpg",
                max_length=500,
            ),
        ),
    ]
