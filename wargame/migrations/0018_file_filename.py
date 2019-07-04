# Generated by Django 2.2.1 on 2019-06-08 20:57
import os
from django.db import migrations, models


def set_filename(apps, schema_editor):
    File = apps.get_model("wargame", "File")
    for file in File.objects.all().iterator():
        file.filename = os.path.basename(file.file.name)
        file.save()


class Migration(migrations.Migration):
    dependencies = [("wargame", "0017_submission_times")]

    operations = [
        migrations.AddField(
            model_name="file",
            name="filename",
            field=models.CharField(default="test", max_length=256),
            preserve_default=False,
        ),
        migrations.RunPython(set_filename),
    ]
