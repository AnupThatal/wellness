# Generated by Django 4.2.6 on 2023-12-09 04:28

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
            name="category",
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
                ("category", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="course",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=1000)),
                ("file_mainpic", models.FileField(upload_to="")),
                ("title", models.TextField(max_length=200)),
                ("Description", models.TextField()),
                ("quotes", models.TextField()),
                ("important_notes", models.TextField()),
                ("price", models.IntegerField()),
                ("pic1", models.FileField(upload_to="")),
                ("pic2", models.FileField(upload_to="")),
                (
                    "offers",
                    models.CharField(
                        blank=True, default="0", max_length=500, null=True
                    ),
                ),
                ("offers_date", models.DateField(blank=True, null=True)),
                ("subject_email", models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="email_subscription",
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
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
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
                ("trainer_name", models.CharField(max_length=150)),
                ("expertise", models.CharField(max_length=1000)),
                ("trainer_pic", models.FileField(upload_to="")),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("India", "India"),
                            ("Nepal", "Nepal"),
                            ("Canada", "Canada"),
                            ("USA", "USA"),
                            ("Australia", "Australia"),
                        ],
                        max_length=100,
                    ),
                ),
                ("location", models.CharField(default="Nepal", max_length=300)),
                ("contact", models.CharField(max_length=20)),
                ("desc", models.TextField()),
                ("title", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="profile",
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
                ("nationality", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("firstname", models.CharField(max_length=200)),
                ("lastname", models.CharField(max_length=300)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Itemcart",
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
                ("items", models.ManyToManyField(to="yogashala.course")),
            ],
        ),
        migrations.CreateModel(
            name="course_buy",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("puja_date", models.DateField()),
                ("Email", models.EmailField(max_length=254)),
                ("contact", models.CharField()),
                ("payment", models.CharField()),
                ("address", models.TextField(max_length=500)),
                ("message", models.TextField(default="")),
                (
                    "paid",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "completed",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "puja_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="yogashala.course",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="trainer_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainers_profile",
                to="yogashala.trainer",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="blog",
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
                ("title", models.CharField(max_length=1000)),
                ("top_content", models.TextField()),
                ("content", models.TextField()),
                ("important_notes", models.TextField()),
                ("main_pic1", models.FileField(upload_to="")),
                ("pic1", models.FileField(upload_to="")),
                ("pic2", models.FileField(upload_to="")),
                ("Date", models.DateField(blank=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="yogashala.category",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
