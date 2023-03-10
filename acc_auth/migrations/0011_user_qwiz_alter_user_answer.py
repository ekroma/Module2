# Generated by Django 4.1.6 on 2023-02-14 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc_auth', '0010_remove_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qwiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='acc_auth.question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='answer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
