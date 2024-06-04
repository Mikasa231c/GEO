
from enum import Enum
from django.db import models

# Create your models here.

class GameType(Enum):
    Final_Fantasy_X = "Final Fantasy X"
    Fifa_2024 = "Fifa 2024"
    Spyro = "spyro"
    LEAGUE_OF_LEGENDS = "League of Legends"
    WORLD_OF_WARCRAFT = "Word of Warcraft"
    NBA_2024 = "NBA 2024"
    Cyber_Punk = "Cyber Punk"

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]



class Game(models.Model):

    GAME_TYPE_CHOICES = [("SPORT", "sport"), ("RPG", "rpg"),("ADVENTURE","adventure"),{"FANTASY","fantasy"}]


    games_type = models.CharField(choices=GAME_TYPE_CHOICES, max_length=20)
    PS4 = models.BooleanField(default=False)
    PS5 = models.BooleanField(default=False)
    PC  = models.BooleanField(default=False)
    Multiplayer_mode = models.BooleanField(default=False)
    games = models.CharField(choices=GameType.choices(), max_length=20)
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=5) #od 000.00 do 999.99

    def __str__(self):
        return f"{self.id}/{self.games_type}/{self.games}/{self.price_per_hour}"
class Klient(models.Model):
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    birth_day = models.DateField()

    def __str__(self):
        return f"{self.id}/{self.mail}"

class Rezerwacja(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, related_name="reservations")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        hours = 1
        #TODO calculate hours from start to end
        self.price = self.game.price_per_hour*hours
        super(Rezerwacja, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.klient.mail}/{self.game}"