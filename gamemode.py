from random import randint
import time

class Computer_Easy_Mode:
    def computer(board, sign):
        '''The computer choose a randint to play on the grid
        
        PARAMETERS -
        board : The grid the game is played on
        sign : The sign the computer will play with
        
        RETURNS -
        sign : Return the sign in the grid to update the game board'''
        while True:
            ai_choice = randint(1, 9)

            if str(ai_choice) not in board:
                continue
            
            else:
                board[ai_choice - 1] = sign
                break

        return sign

    def gamemode1player_easy_mode(board, win, players, ai_sign):
        '''The process to play the game in easy mode
        
        PARAMETERS -
        board : The grid the game is played on
        win : To check if someone win
        players : Take the actual player sign to check if it is the program turn or not
        ai_sign : Dynamic way to change the computer sign without changing everything 
        
        RETURNS - 
        return combo : check if any combo is valid, then return it to valid the win
        return None : return nothing and continue the game if there's no winner'''
        if players == ai_sign:
            Computer_Easy_Mode.computer(board, ai_sign)

            for combo in win:
                if all(board[ai_sign] == players for ai_sign in combo):
                    return combo
                
            return None
        
        else:

            tableau(board)

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
        
class Computer_Normal_Mode:
    def computer_normal_mode(board, sign):

        '''The computer play on a predefined cell if the player is about to win (not taking all the winning cond to be beatable), or play a randint
        
        PARAMETERS -
        board : The grid the game is played on
        sign : The sign the computer will play with
        
        RETURNS -
        sign : Return the sign in the grid to update the game board'''

        while True:
            ai_choice = randint(1, 9)

            if board[0] and board[1] == "X" and not board[2] == "O":
                board[2] = sign
                break
            
            elif board[3] and board[4] == "X" and not board[5] == "O":
                board[5] = sign
                break
            
            elif board[6] and board[7] == "X" and not board[8] == "O":
                board[8] = sign
                break
            
            elif board[0] and board[3] == "X" and not board[6] == "O":
                board[6] = sign
                break
            
            elif board[1] and board[4] == "X" and not board[7] == "O":
                board[7] = sign
                break

            elif board[2] and board[5] == "X" and not board[8] == "O":
                board[8] = sign
                break
            
            elif board[0] and board[4] == "X" and not board[8] == "O":
                board[8] = sign
                break

            elif board[2] and board[4] == "X" and not board[6] == "O":
                board[6] = sign
                break

            elif str(ai_choice) not in board:
                continue
            
            else:
                board[ai_choice - 1] = sign
                break
        return sign

    def gamemode1player_normal_mode(board, win, players, ai_sign):
        '''The process to play the game in normal mode
        
        PARAMETERS -
        board : The grid the game is played on
        win : To check if someone win
        players : Take the actual player sign to check if it is the program turn or not
        ai_sign : Dynamic way to change the computer sign without changing everything 
        
        RETURNS - 
        return combo : check if any combo is valid, then return it to valid the win
        return None : return nothing and continue the game if there's no winner'''

        if players == ai_sign:
            Computer_Normal_Mode.computer_normal_mode(board, ai_sign)

            for combo in win:
                if all(board[ai_sign] == players for ai_sign in combo):
                    return combo
                
            return None
        
        else:

            tableau(board)

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

def restart_choice():
    '''Reusable code to let the player choose to replay or not
    
    RETURNS -
    quit() : Return to quit the program if the player decide to stop the game'''
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

def tableau(board):
        '''Reusable code to display the board game
        
        PARAMETERS - 
        board : To use the actual grid game'''

        print("\n", " | ".join(board[:3]))
        print("---+---+---")
        print("", " | ".join(board[3:6]))
        print("---+---+---")
        print("", " | ".join(board[6:]))

def gamemode2player(board, win, players):

    '''The process to play the game with 2 players
        
    PARAMETERS -
    board : The grid the game is played on
    win : To check if someone win
    players : Take the actual player sign to check which player turn it is
    
    RETURNS - 
    return combo : check if any combo is valid, then return it to valid the win
    return None : return nothing and continue the game if there's no winner'''

    tableau(board)

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
