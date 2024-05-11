from django.core.management.base import BaseCommand
from movies.models import Movie
from itertools import islice

def row_to_movie(row):
    tconst, type, primary_title, original_title, is_adult, year, _, runtime = row.split('\t')[:8]

    if is_adult != '0':
        return None

    if type != 'short' and type != 'movie':
        return None

    new_movie = Movie(
        tconst=tconst,
        type=type,
        primary_title=primary_title,
        original_title=original_title,
    )

    try:
        new_movie.year = int(year)
    except ValueError:
        pass

    try:
        new_movie.runtime = int(runtime)
    except ValueError:
        pass

    return new_movie

class Command(BaseCommand):
    help = 'Loads entries from IMDb\'s title.basics file'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Loading from {options['data_file']}')
        new_movies = []
        count = 0
        for row in islice(open(options['data_file']), 1, None):
            new_movie = row_to_movie(row)
            if not new_movie:
                continue
            new_movies.append(row_to_movie(row))
            if len(new_movies) >= 100000:
                Movie.objects.bulk_create(new_movies)
                count += len(new_movies)
                self.stdout.write(str(count))
                new_movies = []

        if len(new_movies) > 0:
            Movie.objects.bulk_create(new_movies)
        self.stdout.write(str(count + len(new_movies)))
