from django.core.management.base import BaseCommand
from movies.models import Person
from itertools import islice

def row_to_person(row):
    nconst, name, year_of_birth, year_of_death = row.split('\t')[:4]
    new_person = Person(nconst=nconst, name=name)

    try:
        new_person.year_of_birth = int(year_of_birth)
    except ValueError:
        pass

    try:
        new_person.year_of_death = int(year_of_death)
    except ValueError:
        pass

    return new_person

class Command(BaseCommand):
    help = 'Loads entries from IMDb\'s name.basics file'

    def add_arguments(self, parser):
        parser.add_argument("data_file", type=str)

    def handle(self, *args, **options):
        self.stdout.write(f'Loading from {options['data_file']}')
        new_people = []
        count = 0
        for row in islice(open(options['data_file']), 1, None):
            new_people.append(row_to_person(row))
            if len(new_people) >= 100000:
                Person.objects.bulk_create(new_people)
                count += len(new_people)
                self.stdout.write(str(count))
                new_people = []

        if len(new_people) > 0:
            Person.objects.bulk_create(new_people)
        self.stdout.write(str(count + len(new_people)))
