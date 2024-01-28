from django.db import models

class Resourcepacks(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(default=0, max_length=128)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ресурспак'
        verbose_name_plural = 'Ресурспаки'
