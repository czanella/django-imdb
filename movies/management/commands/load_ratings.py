from django.core.management.base import BaseCommand
from movies.models import Movie
from itertools import islice
from datetime import datetime

class Command(BaseCommand):
    help = 'Loads entries from IMDb\'s title.ratings file'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Loading from {options['data_file']}')
        start = datetime.now()
        ratings = {
            tconst:{ 'rating': float(rating), 'votes': int(votes) }
            for (tconst, rating, votes)
            in map(
                lambda r:r.split('\t')[:3],
                islice(open(options['data_file']), 1, None),
            )
        }
        self.stdout.write(f'done {str(datetime.now() - start)}')
        self.stdout.write('Updating movies...')
        movies = list(Movie.objects.all())
        for movie in movies:
            rating = ratings.get(movie.tconst, { 'rating': 0.0, 'votes': 0 })
            movie.rating = rating['rating']
            movie.rating_votes = rating['votes']
        self.stdout.write(f'done {str(datetime.now() - start)}')
        self.stdout.write('Writing to database...')
        Movie.objects.bulk_update(movies, ['rating', 'rating_votes'])
        self.stdout.write(f'done {str(datetime.now() - start)}')
