# Generated by Django 5.1.4 on 2024-12-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_on_vacation',
            field=models.BooleanField(default=False),
        ),
    ]
