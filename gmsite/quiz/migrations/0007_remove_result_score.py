# Generated by Django 4.0.4 on 2022-06-19 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_result_hiscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='score',
        ),
    ]