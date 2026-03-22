import tkinter as tk
 
def click(event):
    global selected, color_to_move, Moves
    if selected == None:
        if  Board[event.y // SQUARE_SIZE][event.x // SQUARE_SIZE] != "." and Board[event.y // SQUARE_SIZE][event.x // SQUARE_SIZE].isupper() == color_to_move:
            selected = (event.y // SQUARE_SIZE, event.x // SQUARE_SIZE)
            Moves = get_moves(Board, selected[0], selected[1])
            print(Moves)
            draw_board (Board)
    else:
        if(event.y // SQUARE_SIZE != selected[0] or event.x // SQUARE_SIZE != selected[1]):
            Board[event.y // SQUARE_SIZE][event.x // SQUARE_SIZE] = Board[selected[0]][selected[1]]
            Board[selected[0]][selected[1]] = "."
            if color_to_move:
                color_to_move = False
            else:
                color_to_move = True
        selected = None
        Moves = []
        draw_board(Board)

def draw_board(board):
    global Moves
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            color = "white" if (i + j) % 2 == 0 else "black"
            if (selected != None and j == selected[0] and i == selected[1]):
                color = "gray"
            if ((j, i) in Moves):
                color = "green"
            x1 = i * SQUARE_SIZE
            y1 = j * SQUARE_SIZE

            canvas.create_rectangle(x1, y1, x1 + SQUARE_SIZE, y1 + SQUARE_SIZE, fill=color, outline="")
    
            p = board[j][i]
            if (p != '.'):
                color = "white" if p.isupper() else "black"
                
                canvas.create_text((x1 + SQUARE_SIZE / 2), (y1 + SQUARE_SIZE / 2) + 2, text= p.capitalize(), font= ("Arial", 50), fill="gray")
                canvas.create_text((x1 + SQUARE_SIZE / 2), (y1 + SQUARE_SIZE / 2) - 2, text= p.capitalize(), font= ("Arial", 50), fill="gray")
                canvas.create_text((x1 + SQUARE_SIZE / 2) - 2, (y1 + SQUARE_SIZE / 2), text= p.capitalize(), font= ("Arial", 50), fill="gray")
                canvas.create_text((x1 + SQUARE_SIZE / 2) + 2, (y1 + SQUARE_SIZE / 2), text= p.capitalize(), font= ("Arial", 50), fill="gray")
                canvas.create_text(x1 + SQUARE_SIZE / 2, y1 + SQUARE_SIZE / 2, text= p.capitalize(), font= ("Arial", 50), fill=color)

def get_moves(board, row, col):
    print (row, col)
    moves = []
    piece = board[row][col]
    color = piece.isupper()
    if piece.lower() == "p":
        print("p")
        if color == False:
            print("b")
           
            if board[row + 1][col] == ".":
                moves.append((row + 1, col))
                if row == 1 and board[row + 2][col] == ".":
                    moves.append((row + 2, col))
            if board[row + 1][col + 1] != "." and board[row + 1][col + 1].isupper() != color:
                moves.append((row + 1, col + 1))
            if board[row - 1][col + 1] != "." and board[row + 1][col - 1].isupper() != color:
                moves.append((row + 1, col - 1))
        else:
            print("w")
            if board[row + 1][col] == ".":
                moves.append((row + 1, col))
                if row == 1 and board[row + 2][col] == ".":
                    moves.append((row + 2, col))
            if board[row + 1][col + 1] != "." and board[row + 1][col + 1].isupper() != color:
                moves.append((row + 1, col + 1))
            if board[row - 1][col + 1] != "." and board[row + 1][col - 1].isupper() != color:
                moves.append((row + 1, col - 1))


    return moves
BOARD_SIZE = 8
SQUARE_SIZE = 80
selected = None
window = tk.Tk()
window.title("Chess Board")
color_to_move = True
 
canvas = tk.Canvas(window, width=640, height=640)
canvas.pack()
Board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","." ],
    [".",".",".",".",".",".",".","." ],
    [".",".",".",".",".",".",".","." ],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"],
]
Moves = []
draw_board(Board)
canvas.bind("<Button-1>", click)          


window.mainloop()

