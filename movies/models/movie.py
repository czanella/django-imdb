from django.db import models

MOVIE_TYPES = {
    'short': 'Short Film',
    'movie': 'Feature Film',
}

class Movie(models.Model):
    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        indexes = [
            models.Index(fields=['primary_title']),
            models.Index(fields=['original_title']),
        ]

    tconst = models.CharField(max_length=16, unique=True)
    type = models.CharField(max_length=16, choices=MOVIE_TYPES, default='movie')
    primary_title = models.CharField(max_length=256)
    original_title = models.CharField(max_length=256)
    year = models.PositiveIntegerField(null=True, blank=True, default=None)
    runtime = models.PositiveIntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return self.primary_title
