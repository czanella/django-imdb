from django.db import models
from django.core.validators import RegexValidator

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

    tconst = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'tt\d{7}',
                message='Value must be "tt" followed by 7 digits',
            ),
        ],
    )
    type = models.CharField(max_length=16, choices=MOVIE_TYPES, default='movie')
    primary_title = models.CharField(max_length=256)
    original_title = models.CharField(max_length=256)
    year = models.PositiveIntegerField(null=True, blank=True, default=None)
    runtime = models.PositiveIntegerField(null=True, blank=True, default=None)
    rating = models.FloatField(default=0.0)
    rating_votes = models.PositiveIntegerField(default=0)

    @property
    def imdb_url(self):
        return f'https://imdb.com/title/{self.tconst}/'

    def __str__(self):
        return self.primary_title
