# Generated by Django 4.1.6 on 2023-02-14 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc_auth', '0007_question_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct',
        ),
    ]
