import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    global secret_number, attempts_left, guess_history
    secret_number = random.randint(1, 100)
    attempts_left = 5
    guess_history = []
    lbl_result.config(text="New game started! Guess a number between 1 and 100. You have 5 attempts.")
    entry_guess.config(state=tk.NORMAL)
    btn_check.config(state=tk.NORMAL)
    btn_start.config(state=tk.DISABLED)
    status_bar.config(text="Attempts left: 5")
    lbl_guess_history.config(text="")

def check_guess():
    global attempts_left, guess_history
    guess = int(entry_guess.get())
    guess_history.append(guess)
    lbl_guess_history.config(text=f"Previous guesses: {guess_history}")
    attempts_left -= 1
    status_bar.config(text=f"Attempts left: {attempts_left}")
    if guess == secret_number:
        lbl_result.config(text=f"Congratulations! You guessed the number {secret_number} correctly.")
        entry_guess.config(state=tk.DISABLED)
        btn_check.config(state=tk.DISABLED)
        btn_start.config(state=tk.NORMAL)
    else:
        if attempts_left > 0:
            if guess < secret_number:
                lbl_result.config(text=f"Try again! Guess higher.")
            else:
                lbl_result.config(text=f"Try again! Guess lower.")
        else:
            lbl_result.config(text=f"Game over! The correct number was {secret_number}.")
            entry_guess.config(state=tk.DISABLED)
            btn_check.config(state=tk.DISABLED)
            btn_start.config(state=tk.NORMAL)

def show_instructions():
    messagebox.showinfo("Instructions", "Guess a number between 1 and 100. You have 5 attempts to guess correctly.")

def clear_guess_history():
    global guess_history
    guess_history = []
    lbl_guess_history.config(text="")

root = tk.Tk()
root.title("Number Guessing Game")

# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

game_menu = tk.Menu(menubar, tearoff=0)
game_menu.add_command(label="New Game", command=start_game)
game_menu.add_command(label="Instructions", command=show_instructions)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Game", menu=game_menu)

# Widgets
lbl_title = tk.Label(root, text="Welcome to the Number Guessing Game!")
lbl_title.pack(pady=10)

btn_start = tk.Button(root, text="Start Game", command=start_game)
btn_start.pack(pady=5)

lbl_result = tk.Label(root, text="Press 'Start Game' to begin.")
lbl_result.pack(pady=10)

entry_guess = tk.Entry(root, width=20, state=tk.DISABLED)
entry_guess.pack(pady=5)

btn_check = tk.Button(root, text="Check Guess", command=check_guess, state=tk.DISABLED)
btn_check.pack(pady=5)

lbl_guess_history = tk.Label(root, text="", wraplength=300)
lbl_guess_history.pack(pady=5)

btn_clear_history = tk.Button(root, text="Clear Guess History", command=clear_guess_history)
btn_clear_history.pack(pady=5)

status_bar = tk.Label(root, text="Attempts left: 5", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
