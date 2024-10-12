# Generated by Django 5.1.2 on 2024-10-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_quizresult"),
    ]

    operations = [
        migrations.AddField(
            model_name="quizresult",
            name="college_email",
            field=models.EmailField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quizresult",
            name="department",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quizresult",
            name="usn",
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
