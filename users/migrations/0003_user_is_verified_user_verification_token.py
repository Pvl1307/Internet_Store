# Generated by Django 4.2.1 on 2023-09-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Статус верификации'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Код верификации'),
        ),
    ]