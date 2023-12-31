# Generated by Django 4.2.4 on 2023-08-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('text', models.TextField(verbose_name='Текст')),
                ('blog_img', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью статьи')),
                ('date_of_creation', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('count_of_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
