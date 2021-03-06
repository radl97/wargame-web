# Generated by Django 2.1.1 on 2018-09-29 11:42

from django.db import migrations


def update_config(apps, schema_editor):
    Config = apps.get_model("wargame_admin", "Config")
    show_qpa_points = Config(
        key="show_qpa_points",
        value="False",
        display_name="Show QPA points",
        description="Show the qpa points column on the scoreboard page",
        possible_values='["False", "True"]',
    )
    show_qpa_points.save()

    qpa_points_multiplier = Config(
        key="qpa_points_multiplier",
        value="1",
        display_name="QPA points multiplier",
        description="The multiplier for the QPA points column on the scoreboard. It can be a number or a fraction.",
    )
    qpa_points_multiplier.save()


class Migration(migrations.Migration):
    dependencies = [("wargame_admin", "0006_auto_20180927_1536")]

    operations = [migrations.RunPython(update_config)]
