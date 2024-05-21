from django.db import models
from django.core.validators import RegexValidator   

class Person(models.Model):
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        indexes = [
            models.Index(fields=['name']),
        ]

    nconst = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'nm\d{7}',
                message='Value must be "nm" followed by 7 digits.',
            ),
        ],
    )
    name = models.CharField(max_length=256)
    year_of_birth = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
    )
    year_of_death = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
    )

    @property
    def imdb_url(self):
        return f'https://imdb.com/name/{self.nconst}/'

    def __str__(self):
        return self.name
