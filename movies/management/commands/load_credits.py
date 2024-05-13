import json
from datetime import datetime
from collections import defaultdict
from django.db import transaction
from django.core.management.base import BaseCommand
from movies.models import Movie, Person, Character, CrewMember
from itertools import islice

def row_to_credit(movie, ordering, person, category, job, characters):
    if category == 'actor' or category == 'actress' or category == 'self':
        name = None
        try:
            name = '|'.join(json.loads(characters))
        except:
            pass
        return Character(
            movie=movie,
            person=person,
            ordering=int(ordering),
            name=name,
            is_self=category == 'self',
        )

    return CrewMember(
        movie=movie,
        person=person,
        ordering=int(ordering),
        job_category=category,
        job=job if job != '\\N' else None,
    )

class Command(BaseCommand):
    help = 'Loads entries from IMDb\'s title.principals file'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Loading from {options['data_file']}')
        start = datetime.now()
        new_credits = defaultdict(lambda:[])
        count = 0

        self.stdout.write('Loading movies...')
        movies = {movie.tconst:movie for movie in Movie.objects.all()}
        self.stdout.write(f'done {datetime.now() - start}')

        self.stdout.write('Loading people...')
        people = {person.nconst:person for person in Person.objects.all()}
        self.stdout.write(f'done {datetime.now() - start}')

        for row in islice(open(options['data_file']), 1, None):
            tconst, ordering, nconst, category, job, characters = row.split('\t')[:6]
            movie = movies.get(tconst, None)
            person = people.get(nconst, None)
            if movie and person:
                new_credit = row_to_credit(
                    movie,
                    ordering,
                    person,
                    category,
                    job,
                    characters,
                )
                new_credits[new_credit.__class__].append(new_credit)

            count += 1
            if count % 100000 == 0:
                self.stdout.write(f'{count} {datetime.now() - start}')
                with transaction.atomic():
                    for imdb_class in new_credits:
                        self.stdout.write(f'Writing {imdb_class.__name__}')
                        imdb_class.objects.bulk_create(new_credits[imdb_class])
                        self.stdout.write(str(datetime.now() - start))
                new_credits = defaultdict(lambda:[])

        for imdb_class in new_credits:
            self.stdout.write(f'Writing last {imdb_class.__name__}')
            imdb_class.objects.bulk_create(new_credits[imdb_class])
            self.stdout.write(str(datetime.now() - start))
