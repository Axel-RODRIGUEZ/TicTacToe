import time
from gamemode import gamemode2player, Computer_Easy_Mode, Computer_Normal_Mode, restart_choice, tableau

combos = (

    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)

)

while True:

    print("")
    gamemode_choice = input("1 - Mode solo\n2 - Mode 2 joueurs\n3 - Quitter\n")
    grid = ["1","2","3","4","5","6","7","8","9"]
    # Solo mode
    if gamemode_choice == "1":
        while True : 
            print("")
            difficulty = input("1 - Mode facile\n2 - Mode normal\n3 - Revenir en arrière\n")
            grid = ["1","2","3","4","5","6","7","8","9"]

            if difficulty == "1":
                    player1 = "X"
                    ai = "O"
                    player = player1

                    for i in range(9):
                        win = Computer_Easy_Mode.gamemode1player_easy_mode(grid, combos, player, ai)

                        if win:       
                            tableau(grid)
                            print(f"Le joueur '{player}' a gagné !")
                            break

                        if player == player1:
                            player = ai
                        
                        else:
                            player = player1

                    else:
                        print("Il y a eu égalité.")

                    restart_choice()

            elif difficulty == "2":
                player1 = "X"
                ai = "O"
                player = player1

                for i in range(9):
                    win = Computer_Normal_Mode.gamemode1player_normal_mode(grid, combos, player, ai)

                    if win:       
                        tableau(grid)
                        print(f"Le joueur '{player}' a gagné !")
                        break

                    if player == player1:
                        player = ai
                    
                    else:
                        player = player1

                else:
                    print("Il y a eu égalité.")

                restart_choice()

            elif difficulty == "3":
                break

            else:
                print("Erreur, veuillez réessayer")
                continue

    # 2 players mode
    elif gamemode_choice == "2":
        player1 = "X"
        player2 = "O"
        player = player1

        for i in range(9):
            win = gamemode2player(grid, combos, player)
            
            if win:       
                tableau(grid)
                print(f"Le joueur '{player}' a gagné !")
                break

            player = player1 if player == player2 else player2

        else:
            print("Il y a eu égalité.")

        restart_choice()

    elif gamemode_choice == "3":
        print("Merci d'avoir joué !")
        break

    else:
        print("Erreur du programme, essayez d'entrer un nombre correct.")
        time.sleep(0.5)
        continue
