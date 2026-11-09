from django.db import models
from django.urls import reverse
from datetime import datetime


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=255, null=False)
#    name_category_ru = models.CharField(max_length=255, default='Новая категория')

    def __str__(self):
#        return self.name_category_ru
        return self.name_category



    def get_absolute_url(self):
        return reverse('cat', kwargs={'category_id': self.pk})

    class Meta:
        db_table = 'categories'


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.TextField()

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'tags'

    def get_absolute_url(self):
        return reverse('wallpapers_by_tag', args=[str(self.id)])


class Wallpapers(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='wallpapers')
    width = models.IntegerField()
    height = models.IntegerField()
    wallp_size = models.FloatField()
    created_up = models.DateTimeField(default=datetime.now)
    path_preview = models.CharField(max_length=255)
    path_original = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('wallp', kwargs={'wallp_id': self.pk})

    class Meta:
        db_table = 'wallpapers'
        ordering = ['-created_up']


class Wallpapers_Tags(models.Model):
    wallpaper_id = models.ForeignKey(
        Wallpapers,
        on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wallpapers_tags'
        unique_together = ('wallpaper_id', 'tag_id')
