# Generated by Django 4.2.6 on 2023-12-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("yogashala", "0012_remove_trainer_title_trainer_email_alter_trainer_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="city",
            field=models.CharField(default="london", max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="trainer",
            name="desc",
            field=models.TextField(blank=True, null=True),
        ),
    ]
