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
        related_name='crew_works',
        on_delete=models.CASCADE,
    )
    job_category = models.CharField(max_length=256)
    job = models.CharField(max_length=256, null=True, blank=True, default=None)
    ordering = models.PositiveIntegerField()

    def __str__(self):
        return ' - '.join(filter(bool, (self.job_category, self.job)))