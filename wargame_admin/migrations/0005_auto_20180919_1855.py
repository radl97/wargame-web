# Generated by Django 2.1.1 on 2018-09-19 16:55

from django.db import migrations


def update_config(apps, schema_editor):
    Config = apps.get_model("wargame_admin", "Config")
    disable_registration = Config(
        key="disable_registration",
        value="False",
        display_name="Disable registration",
        description="Do not allow new users to register",
        possible_values='["False", "True"]',
    )
    disable_registration.save()


class Migration(migrations.Migration):
    dependencies = [("wargame_admin", "0004_auto_20180815_1843")]

    operations = [migrations.RunPython(update_config)]
