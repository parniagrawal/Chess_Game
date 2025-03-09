import tkinter as tk
import chess

def make_move():
    move = move_entry.get()
    try:
        board.push_san(move)
        update_board()
        move_entry.delete(0, tk.END)
        if board.is_checkmate():
            tk.messagebox.showinfo("Game Over", "Checkmate! Game Over.")
        elif board.is_stalemate():
            tk.messagebox.showinfo("Game Over", "Stalemate! Game Over.")
    except ValueError:
        tk.messagebox.showerror("Invalid Move", "Please enter a valid move in SAN notation.")

def update_board():
    board_text.set(str(board))

# Initialize game board
board = chess.Board()

# Create main window
root = tk.Tk()
root.title("Chess Game")
root.geometry("400x400")

board_text = tk.StringVar()
board_label = tk.Label(root, textvariable=board_text, font=("Courier", 12), justify="left")
board_label.pack(pady=10)

move_entry = tk.Entry(root, width=20)
move_entry.pack(pady=5)

move_button = tk.Button(root, text="Make Move", command=make_move)
move_button.pack(pady=5)

update_board()
root.mainloop()
