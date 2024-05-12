from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        indexes = [
            models.Index(fields=['name']),
        ]

    nconst = models.CharField(max_length=16, unique=True)
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

    def __str__(self):
        return self.name