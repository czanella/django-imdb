from django.db import models
from .movie import Movie
from .person import Person

class CrewMember(models.Model):
    class Meta:
        verbose_name = 'crew member'
        verbose_name_plural = 'crew members'
        indexes = [
            models.Index(fields=['job_category']),
            models.Index(fields=['job']),
        ]

    movie = models.ForeignKey(
        Movie,
        related_name='crew_members',
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        Person,
        related_name='movies_as_crew',
        on_delete=models.CASCADE,
    )
    job_category = models.CharField(max_length=256)
    job = models.CharField(max_length=256)
