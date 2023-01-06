from django.db import models


class Post(models.Model):
    """
    Посты - подкатегории основного меню.
    """
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        blank=True,
        related_name='posts'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children'
    )

    class Meta:
        verbose_name = 'Item menu'
        verbose_name_plural = 'Items menu'

    def __str__(self):
        return self.title


class Menu(models.Model):
    """
    Модель в БД основного меню.
    """
    title = models.CharField('Menu title', max_length=255, unique=True)
    slug = models.SlugField('Menu slug', max_length=255)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu_more'

    def __str__(self):
        return self.title
