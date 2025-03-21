def minimax(board, depth, is_max):
    scores = {'X': 1, 'O': -1, 'draw': 0}
    
    winner = check_winner(board)
    if winner: return scores[winner]
    
    moves = [i for i in range(9) if board[i] == " "]
    
    if is_max:
        best = -float('inf')
        for move in moves:
            board[move] = 'X'
            best = max(best, minimax(board, depth + 1, False))
            board[move] = " "
        return best
    else:
        best = float('inf')
        for move in moves:
            board[move] = 'O'
            best = min(best, minimax(board, depth + 1, True))
            board[move] = " "
        return best

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return "draw" if " " not in board else None

board = ["X", "O", "X", " ", "O", " ", " ", "X", " "]
print(minimax(board, 0, True))
