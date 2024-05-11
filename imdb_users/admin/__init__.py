from django.contrib import admin
from .imdb_user import ImdbUserAdmin
from imdb_users.models import ImdbUser

admin.site.register(ImdbUser, ImdbUserAdmin)
