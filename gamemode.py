from random import randint
import time

def restart_choice():
    while True:
            restart_choice = input("Voulez-vous rejouer ? (O/N)\n").lower()

            if restart_choice == "o":
                break
            
            elif restart_choice == "n":
                print("Merci d'avoir joué !")
                return quit()

            else:
                print("Erreur, veuillez réessayer")
                time.sleep(0.5)
                continue
    return None

def computer(board, sign):

    while True:
        ai_choice = randint(1, 9)

        if str(ai_choice) not in board:
            continue
        
        else:
            board[ai_choice - 1] = sign
            break

    return sign

def gamemode1player(board, win, players, ai_sign):

    if players == ai_sign:
        computer(board, ai_sign)

        for combo in win:
            if all(board[ai_sign] == players for ai_sign in combo):
                return combo
            
        return None
    
    else:

        print("\n", " | ".join(board[:3]))
        print("---+---+---")
        print("", " | ".join(board[3:6]))
        print("---+---+---")
        print("", " | ".join(board[6:]))

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

        for combo in win:
            if all(board[choice] == players for choice in combo):
                return combo
            
        return None



def gamemode2player(board, win, players):

    print("\n", " | ".join(board[:3]))
    print("---+---+---")
    print("", " | ".join(board[3:6]))
    print("---+---+---")
    print("", " | ".join(board[6:]))

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

    for combo in win:
        if all(board[choice] == players for choice in combo):
            return combo
        
    return None
