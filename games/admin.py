from django.contrib import admin

from games.models import Game, Reminder

admin.site.register(Game)
admin.site.register(Reminder)