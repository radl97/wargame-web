# Generated by Django 2.0.3 on 2018-04-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wargame', '0003_challenge_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
    ]
