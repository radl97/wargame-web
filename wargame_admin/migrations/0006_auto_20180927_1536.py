# Generated by Django 2.1.1 on 2018-09-27 13:36

from django.db import migrations


def update_config(apps, schema_editor):
    Config = apps.get_model("wargame_admin", "Config")
    wargame_active = Config(
        key="wargame_active",
        value="True",
        display_name="Wargame active",
        description="Allow users to view challenges, submit answers, view hints, and download files",
        possible_values='["False", "True"]',
    )
    wargame_active.save()


class Migration(migrations.Migration):
    dependencies = [("wargame_admin", "0005_auto_20180919_1855")]

    operations = [migrations.RunPython(update_config)]
