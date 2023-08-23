from django.db import models

NULLABLE = {'blank': True, 'null': True}


class WeBlog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Текст')
    blog_img = models.ImageField(upload_to='blog/', verbose_name='Превью статьи', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    count_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return (f'Название: {self.title}'
                f'Дата создания: {self.date_of_creation}'
                f'Опубликовано: {self.is_published}')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
