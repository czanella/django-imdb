# Django Rest Framework + iMDB

This is a sample Django Rest Framework app made to outline DRF's basic features. It's an API to store and retrieve movie data based on [iMDB's free datasets](https://datasets.imdbws.com/).

## Development and set up

The project has a `docker-compose.yml` file designed to quickly set up a development environment. The `docker compose up` command should build a Postgres image and a Django image, and create containers with the app. You can then access http://localhost:8000/api/ to check the API browser or http://localhost:8000/admin/ for the traditional Django admin.

## Populating the database

At this point the API is already usable, but to make it more interesting you can populate it with the datasets provided by iMDB. Follow these steps:

1. Navigate to https://datasets.imdbws.com/ and download and extract the following files:
* title.basics.tsv
* name.basics.tsv
* title.principals.tsv
* title.ratings.tsv

2. Run the following commands, in this order:
* `python manage.py load_movies <path to title.basics.tsv>` - loads movie information
* `python manage.py load_people <path to name.basics.tsv>` - loads people information
* `python manage.py load_credits <path to title.principals.tsv>` - loads information about characters and crew members
* `python manage.py load_ratings <path to title.ratings.tsv>` - loads rating scores for movies

These datasets are fairly large and take a while to run - some might take around 10 minutes, but the heavier ones, like `load_credits` can take several hours.