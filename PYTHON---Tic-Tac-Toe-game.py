def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    return all(all(cell != " " for cell in row) for row in board)

def take_turn(board, player):
    while True:
        try:
            row = int(input(f"{player}'s turn. Enter row (0-2): "))
            col = int(input(f"{player}'s turn. Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken.")
        except (ValueError, IndexError):
            print("Please enter a valid row and column.")

def switch_player(player):
    return "O" if player == "X" else "X"

def play_game():
    board = initialize_board()
    current_player = "X"
    while True:
        print_board(board)
        take_turn(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = switch_player(current_player)

if __name__ == "__main__":
    play_game()
