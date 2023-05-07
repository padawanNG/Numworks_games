# Initialisation du tableau de jeu
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Définition de la fonction qui affiche le tableau de jeu
def display_board():
  print("")  
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Fonction qui demande au joueur de saisir sa position et valide la saisie
def handle_turn(player): 
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  board[position] = player
  display_board()

# Fonction qui vérifie s'il y a un gagnant
def check_win():
  global game_still_going
  # Vérifier les lignes
  row_winner = check_rows()
  # Vérifier les colonnes
  column_winner = check_columns()
  # Vérifier les diagonales
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  if winner == "X" or winner == "O":
    print(winner + " won!")
    game_still_going = False

# Fonction qui vérifie les lignes pour un gagnant
def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None

# Fonction qui vérifie les colonnes pour un gagnant
def check_columns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None

# Fonction qui vérifie les diagonales pour un gagnant
def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None

# Fonction qui vérifie s'il y a égalité
def check_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    print("Tie!")

# Fonction principale qui gère le déroulement du jeu
def play_game():
  # Afficher le tableau de jeu vide
  display_board()
  # Tant que le jeu est en cours
  while game_still_going:
    # Gérer le tour du joueur X
    handle_turn("X")
    # Vérifier s'il y a un gagnant après le tour du joueur X
    check_win()
    # Vérifier s'il y a égalité après le tour du joueur X
    check_tie()
    # Gérer le tour du joueur O
    if game_still_going:
      handle_turn("O")
      # Vérifier s'il y a un gagnant après le tour du joueur O
      check_win()
      # Vérifier s'il y a égalité après le tour du joueur O
      check_tie()

# Initialiser la variable qui indique si le jeu est en cours
game_still_going = True
# Lancer le jeu


print("======================")
print(" Début du programme ! ")
print("======================")

play_game()

print("")
print("====================")
print(" Fin du programme ! ")
print("====================")



