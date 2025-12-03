import time
from gamemode import gamemode2player, gamemode1player, restart_choice

combos = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

while True:

    grid = ["1","2","3","4","5","6","7","8","9"]

    gamemode_choice = input("1 - Mode solo\n2 - Mode 2 joueurs\n")

    # Solo mode
    if gamemode_choice == "1":

        player1 = "X"
        ai = "O"
        player = player1

        for i in range(9):

            win = gamemode1player(grid, combos, player, ai)

            if win:       
                print(f"Le joueur '{player}' a gagné !")
                break

            if player == player1:
                player = ai
            
            else:
                player = player1

        else:
            print("Il y a eu égalité.")

        restart_choice()

    # 2 players mode
    elif gamemode_choice == "2":

        player1 = "X"
        player2 = "O"
        player = player1

        for i in range(9):

            win = gamemode2player(grid, combos, player)
            
            if win:       
                print(f"Le joueur '{player}' a gagné !")
                break

            player = player1 if player == player2 else player2

        else:

            print("Il y a eu égalité.")

        restart_choice()

    # Error input for the choice of gamemode
    else:
        print("Erreur du programme, essayez d'entrer un nombre correct.")
        time.sleep(0.5)
        continue
