# Generated by Django 4.1.6 on 2023-02-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc_auth', '0005_remove_choice_votes_remove_question_choices_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
