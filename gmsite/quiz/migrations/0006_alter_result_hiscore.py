# Generated by Django 4.0.4 on 2022-06-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_result_hiscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='hiscore',
            field=models.JSONField(default=list),
        ),
    ]
