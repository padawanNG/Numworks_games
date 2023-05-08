import random


# Fonction pour afficher le plateau de jeu
def display_board(board):
    print("")
    print("  A B C D E F G H")
    print(" +---------------+")
    for i in range(8):
        print(str(i+1)+"|", end="")
        for j in range(8):
            if board[i][j] == " ":
                print(" |", end="")
            else:
                print(board[i][j]+"|", end="")
        print()
    print(" +---------------+")

# Fonction pour initialiser le plateau de jeu
def create_board():
    board = []
    for i in range(8):
        board.append([" "] * 8)
    board[3][3], board[4][4] = "O", "O"
    board[3][4], board[4][3] = "X", "X"
    return board

# Fonction pour vérifier si un coup est valide
def is_valid_move(board, row, col, color):
    if board[row][col] != " ":
        return False
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for direction in directions:
        r, c = row, col
        r += direction[0]
        c += direction[1]
        if r < 0 or r >= 8 or c < 0 or c >= 8:
            continue
        if board[r][c] == " " or board[r][c] == color:
            continue
        r += direction[0]
        c += direction[1]
        while r >= 0 and r < 8 and c >= 0 and c < 8:
            if board[r][c] == " ":
                break
            if board[r][c] == color:
                return True
            r += direction[0]
            c += direction[1]
    return False

# Fonction pour retourner les pions après un coup
def flip_tiles(board, row, col, color):
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    board[row][col] = color
    for direction in directions:
        r, c = row, col
        r += direction[0]
        c += direction[1]
        if r < 0 or r >= 8 or c < 0 or c >= 8:
            continue
        if board[r][c] == " " or board[r][c] == color:
            continue
        r += direction[0]
        c += direction[1]
        while r >= 0 and r < 8 and c >= 0 and c < 8:
            if board[r][c] == " ":
                break
            if board[r][c] == color:
                r -= direction[0]
                c -= direction[1]
                while board[r][c] != color:
                    board[r][c] = color
                    r -= direction[0]
                    c -= direction[1]
                break
            r += direction[0]
            c += direction[1]

# Fonction pour retourner le joueur suivant
def next_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

# Fonction pour déterminer le gagnant
def determine_winner(board):
    x_count = 0
    o_count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "X":
                x_count += 1
            elif board[i][j] == "O":
                o_count += 1
    if x_count > o_count:
        return "X"
    elif o_count > x_count:
        return "O"
    else:
        return "Tie"

# Fonction pour jouer une partie complète
def play_game():
    board = create_board()
    current_player = "X"
    while True:
        display_board(board)
        if not any(is_valid_move(board, i, j, current_player) for i in range(8) for j in range(8)):
            break
        row, col = get_move(board, current_player)
        flip_tiles(board, row, col, current_player)
        current_player = next_player(current_player)
    display_board(board)
    winner = determine_winner(board)
    if winner == "Tie":
        print("La partie est nulle !")
    else:
        print("Le joueur", winner, "gagne !")

# Fonction pour demander un coup au joueur
def get_move(board, player):
    while True:
        move = input("Joueur " + player + ", entrez votre coup (ex A1) : ")
        if len(move) == 2 and move[0].isalpha() and move[1].isdigit():
            col = ord(move[0].upper()) - ord("A")
            row = int(move[1]) - 1
            if is_valid_move(board, row, col, player):
                return row, col
        print("Coup invalide, veuillez réessayer.")

# Fonction pour le menu principal
def main_menu():
    print("Bienvenue dans Othello !")
    while True:
        print("Que voulez-vous faire ?")
        print("1. Jouer contre l'ordinateur")
        print("2. Jouer à deux joueurs")
        print("3. Quitter")
        choice = input("Entrez votre choix (1-3) : ")
        if choice == "1":
            play_game_single()
        elif choice == "2":
            play_game_multi()
        elif choice == "3":
            print("Merci d'avoir joué à Othello !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Fonction pour jouer une partie contre l'ordinateur
def play_game_single():
    board = create_board()
    current_player = "X"
    while True:
        display_board(board)
        if not any(is_valid_move(board, i, j, current_player) for i in range(8) for j in range(8)):
            break
        if current_player == "X":
            row, col = get_move(board, current_player)
        else:
            print("L'ordinateur joue...")
            row, col = get_computer_move(board, current_player)
            print("L'ordinateur joue en", chr(col + ord("A")) + str(row + 1))
        flip_tiles(board, row, col, current_player)
        current_player = next_player(current_player)
    display_board(board)
    winner = determine_winner(board)
    if winner == "Tie":
        print("La partie est nulle !")
    else:
        print("Le joueur", winner, "gagne !")

# Fonction pour demander un coup à l'ordinateur
def get_computer_move(board, player):
    valid_moves = [(i,j) for i in range(8) for j in range(8) if is_valid_move(board, i, j, player)]
    return random.choice(valid_moves)

# Fonction pour jouer une partie à deux joueurs
def play_game_multi():
    board = create_board()
    current_player = "X"
    while True:
        display_board(board)
        if not any(is_valid_move(board, i, j, current_player) for i in range(8) for j in range(8)):
            break
        row, col = get_move(board, current_player)
        flip_tiles(board, row, col, current_player)
        current_player = next_player(current_player)
    display_board(board)
    winner = determine_winner(board)
    if winner == "Tie":
        print("La partie est nulle !")
    else:
        print("Le joueur", winner, "gagne !")

            

# Lancer une partie
main_menu()
