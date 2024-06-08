
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ValidationError
from django.views.generic import ListView, DetailView
from reservations.forms import ConfirmReservationForm
from reservations.models import Game, Klient, Rezerwacja

class GamesListViews(ListView):
    model = Game
    template_name = "games_list.html"

class GameDetailView(DetailView):
    model = Game
    template_name = "game_detail.html"

def confirm_reservation(request, game_id):
    # REQUEST METHODS
    # GET
    # POST
    # PUT
    # DELETE
    message = ""
    if request.method == "POST":
        form = ConfirmReservationForm(request.POST)
        if form.is_valid():
            klient, created = Klient.objects.get_or_create(mail=form.cleaned_data["mail"],
                                                           defaults={"phone": form.cleaned_data["phone"],
                                                                     "birth_day": form.cleaned_data["birth_day"]})
            print("Mam klienta")
            game = get_object_or_404(Game, id=game_id)
            print("mam gre")
            if not game.reservations.exists():
                rezerwacja = Rezerwacja.objects.create(klient=klient, game=game)
                print(f"Stworzono rezerwacje {rezerwacja}")
                return redirect("game-list")
            else:
                form = ConfirmReservationForm()
                message = "Ta gra jest juz zarezerwowana"
                print(message)
    else:
        form = ConfirmReservationForm()

    return render(request, "confirm_reservation.html", {"form": form, "game_id": game_id, "message": message})