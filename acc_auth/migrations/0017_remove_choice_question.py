# Generated by Django 4.1.6 on 2023-02-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc_auth', '0016_alter_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
    ]