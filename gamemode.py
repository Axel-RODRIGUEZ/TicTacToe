def gamemode2player(board, win, players):

    # Print the grid    
    print("\n", " | ".join(board[:3]))
    print("---+---+---")
    print("", " | ".join(board[3:6]))
    print("---+---+---")
    print("", " | ".join(board[6:]))

    # Game loop 
    while True:
        try:
            choice = int(input(f"{players}, Choisissez un numéro : "))
            if str(choice) not in board:
                raise ValueError
            else:
                board[choice-1] = players
                break

        except ValueError:
            print("Entrez un nombre valide ")

    # Win condition
    for combo in win:
        if all(board[choice] == players for choice in combo):
            return combo
        
    # No return if no player win 
    return None
