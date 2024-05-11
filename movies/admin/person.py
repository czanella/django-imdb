from django.contrib import admin

from movies.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = (
        'nconst',
        'name',
        'year_of_birth',
        'year_of_death',
    )
    list_display = (
        'nconst',
        'name',
    )