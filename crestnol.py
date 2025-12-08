import os
import random

if not os.path.exists("statistics"):
    os.makedirs("statistics")

def save_statistics(result):
    with open("statistics/stats.txt", "a") as f:
        f.write(result + "\n")

def print_board(board):
    size = len(board)
    print("   " + "   ".join(str(i+1) for i in range(size)))
    for i in range(size):
        row = " | ".join(board[i])
        print(f"{i+1} {row}")
        if i != size - 1:
            print("  " + "----" * size)
    print()

def check_winner(board):
    size = len(board)
    for i in range(size):
        if board[i][0] != " " and all(board[i][j] == board[i][0] for j in range(size)):
            return board[i][0]
    for i in range(size):
        if board[0][i] != " " and all(board[j][i] == board[0][i] for j in range(size)):
            return board[0][i]
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]
    if board[0][size-1] != " " and all(board[i][size-1-i] == board[0][size-1] for i in range(size)):
        return board[0][size-1]
    if all(board[i][j] != " " for i in range(size) for j in range(size)):
        return "Ничья"
    return None

def player_move(board, player):
    size = len(board)
    while True:
        try:
            move = input(f"Ход игрока {player}. Введите номер строки и столбца (например: 1 2): ")
            row, col = map(int, move.split())
            if 1 <= row <= size and 1 <= col <= size and board[row-1][col-1] == " ":
                board[row-1][col-1] = player
                break
            else:
                print("Некорректный ход, попробуйте снова.")
        except:
            print("Некорректный ввод, попробуйте снова.")

def robot_move(board, player):
    size = len(board)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if board[i][j] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = player
    print(f"Робот ({player}) делает ход: {row+1} {col+1}")

def play_game():
    while True:
        while True:
            try:
                size = int(input("Введите размер поля (3-9): "))
                if 3 <= size <= 9:
                    break
                else:
                    print("Некорректный размер, попробуйте снова.")
            except:
                print("Некорректный ввод, введите число.")

        mode = ""
        while mode not in ["1", "2"]:
            mode = input("Выберите режим: 1) Игрок против Игрока 2) Игрок против Робота: ")

        board = [[" " for _ in range(size)] for _ in range(size)]
        current_player = random.choice(["X", "O"])
        print(f"{current_player} ходит первым!")

        while True:
            print_board(board)
            if mode == "1" or (mode == "2" and current_player == "X"):
                player_move(board, current_player)
            else:
                robot_move(board, current_player)

            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "Ничья":
                    print("Ничья!")
                    save_statistics("Ничья")
                else:
                    print(f"Победил {winner}!")
                    save_statistics(f"Победил {winner}")
                break

            current_player = "O" if current_player == "X" else "X"

        again = input("Сыграть еще раз? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за игру!")
            break

play_game()