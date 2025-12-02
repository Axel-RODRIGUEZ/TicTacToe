# Import functions from other files

from gamemode import gamemode2player, gamemode1player

# Listing each combos that lead to winning

combos = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

# List that appear in the TicTacToe before a sign is applied
grid = ["1","2","3","4","5","6","7","8","9"]

# Player creation
player1 = "X"
player2 = "O"
player = player1

gamemode_choice = input("1 - Mode solo\n2 - Mode 2 joueurs")

if gamemode_choice == "1":
        # Player creation
    player1 = "X"
    ai = "O"
    player = player1

    # Game loop until winner
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
        # 9 moves without a win is a draw
        print("Il y a eu égalité.")

elif gamemode_choice == "2":
    # Player creation
    player1 = "X"
    player2 = "O"
    player = player1

    # Game loop until winner
    for i in range(9):

        win = gamemode2player(grid, combos, player)
        
        if win:       
            print(f"Le joueur '{player}' a gagné !")
            break

        player = player1 if player == player2 else player2

    else:

        # 9 moves without a win is a draw
        print("Il y a eu égalité.")

else:
    print("Erreur du programme, essayez d'entrer un nombre correct.")
