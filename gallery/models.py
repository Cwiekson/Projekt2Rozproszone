from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField('Tytuł', max_length=200)
    subtitle = models.CharField('Podtytuł', max_length=200)
    date = models.IntegerField('Rok')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Zdjęcie'
        verbose_name_plural = 'Zdjęcia'
