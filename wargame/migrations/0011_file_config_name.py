# Generated by Django 2.1.1 on 2018-10-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("wargame", "0010_auto_20180920_1617")]

    operations = [
        migrations.AddField(
            model_name="file",
            name="config_name",
            field=models.CharField(choices=[("qpa", "qpa"), ("hacktivity", "hacktivity")], default="qpa", max_length=20),
            preserve_default=False,
        )
    ]
