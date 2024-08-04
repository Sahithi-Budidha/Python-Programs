import tkinter as tk
from tkinter import messagebox

# Tic Tac Toe Board
board = [''] * 9

# Current player
current_player = 'X'

# Check for a win
def check_for_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                       (0, 4, 8), (2, 4, 6)]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != '':
            return True
    return False

# Check for a draw
def check_for_draw():
    return ' ' not in board

# Reset the game
def reset_game():
    global board, current_player
    board = [''] * 9
    current_player = 'X'
    for i in range(9):
        buttons[i].config(text='', state=tk.ACTIVE)

# Button clicked
def button_click(index):
    global current_player
    if board[index] == '':
        buttons[index].config(text=current_player, state=tk.DISABLED)
        board[index] = current_player
        if check_for_win():
            messagebox.showinfo('Tic Tac Toe', f'Player {current_player} wins!')
            reset_game()
        elif check_for_draw():
            messagebox.showinfo('Tic Tac Toe', 'It\'s a draw!')
            reset_game()
        current_player = 'O' if current_player == 'X' else 'X'

# Create the buttons
buttons = []
for i in range(9):
    buttons.append(tk.Button(root, text='', font=('Arial', 20), 
                              width=4, height=2, 
                              command=lambda i=i: button_click(i)))
    buttons[i].grid(row=i // 3, column=i % 3)

# Run the game
root = tk.Tk()
root.title('Tic Tac Toe')
root.mainloop()
