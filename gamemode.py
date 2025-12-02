from random import randint
import time

def restart_choice():
    # Loop to handle an error
    while True:
            # Asking the player
            restart_choice = input("Voulez-vous rejouer ? (O/N)").lower()

            # Breaking the actual while true, leading to the game while true
            if restart_choice == "o":
                break
            
            # quit the program even if there's more than one loop
            elif restart_choice == "n":
                print("Merci d'avoir joué !")
                return quit()

            # Error -> Program loop on the choice
            else:
                print("Erreur, veuillez réessayer")
                time.sleep(0.5)
                continue
    return None

def computer(board, sign):
    # Loop to handle errors
    while True:
        # Algo choosing a random int
        ai_choice = randint(1, 9)

        # Checking if ai is choosing a valid number
        if str(ai_choice) not in board:
            continue
        
        # Changing the number in the board by the sign of the ai
        else:
            board[ai_choice - 1] = sign
            break
    # Return the changes
    return sign

def gamemode1player(board, win, players, ai_sign):

    # Checking if the player of the turn is the ai or not
    if players == ai_sign:
        # If so, it lead to the computer function
        computer(board, ai_sign)
        # Checking after he choose if he won or not
        for combo in win:
            if all(board[ai_sign] == players for ai_sign in combo):
                return combo
        return None
    
    # re-using the function to handle player turn
    else:
        gamemode2player(board, win, players)


def gamemode2player(board, win, players):

    # Print the grid    
    print("\n", " | ".join(board[:3]))
    print("---+---+---")
    print("", " | ".join(board[3:6]))
    print("---+---+---")
    print("", " | ".join(board[6:]))

    # Game loop (same as the player loop in the 1 player gamemode)
    while True:
        try:
            choice = input(f"{players}, Choisissez un numéro : ")

            if choice not in board:
                raise ValueError
            
            else:
                board[int(choice) - 1] = players
                break

        except ValueError:
            print("Entrez un nombre valide ")

    # Win condition
    for combo in win:
        if all(board[choice] == players for choice in combo):
            return combo
        
    # No return if no player win 
    return None
