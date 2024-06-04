
# Register your models here.
from django.contrib import admin

from reservations.models import Game, Klient, Rezerwacja

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fields = ["games_type", "PS4", "PS5", "PC", "Multiplayer_mode", "games", "price_per_hour"]
    list_display = ["games_type", "PS4", "PS5", "PC", "Multiplayer_mode", "games", "price_per_hour"]
    readonly_fields = ["id", ]

class KlientAdmin(admin.ModelAdmin):
    fields = ["mail", "phone", "birth_day"]
    list_display = ["mail", "phone", "birth_day"]


class RezerwacjaAdmin(admin.ModelAdmin):
    field = ["date_created", "klient", "game", "price"]
    list_display = ["date_created", "klient", "game", "price"]
    readonly_fields = ["price", "date_created"]

admin.site.register(Klient, KlientAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Rezerwacja, RezerwacjaAdmin)