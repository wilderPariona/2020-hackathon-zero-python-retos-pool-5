from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    options_winner = {"piedra":"tijeras", "papel":"piedra", "tijeras":"papel"}
    if(ai == player):
        return "Empate!"
    elif(ai == options_winner[player]):
        return "Ganaste!"
    else:
        return "Perdiste!"

# Entry Point
def Game():
    player = input("Introduce piedra papel o tijera: ")
    ai = options[randint(0,2)]

    winner = quienGana(player, ai)

    print(winner)

Game()
