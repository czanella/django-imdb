from django.db import models
from .movie import Movie
from .person import Person

class Character(models.Model):
    class Meta:
        verbose_name = 'character'
        verbose_name_plural = 'characters'
        indexes = [
            models.Index(fields=['name']),
        ]

    movie = models.ForeignKey(
        Movie,
        related_name='characters',
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        Person,
        related_name='characters',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=512, null=True, blank=True, default=None)
    ordering = models.PositiveIntegerField()
    is_self = models.BooleanField(default=False)

    def __str__(self):
        return '<no name>' if self.name is None else self.name
