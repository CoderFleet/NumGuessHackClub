import tkinter as tk
from tkinter import messagebox
import random

# Global variables
minimum_number = 1
maximum_number = 100
secret_number = 0
attempts_left = 5
guess_history = []

def start_game():
    global secret_number, attempts_left, guess_history
    secret_number = random.randint(minimum_number, maximum_number)
    attempts_left = 5
    guess_history = []
    lbl_result.config(text=f"Let's start a new game! Try to guess a number between {minimum_number} and {maximum_number}. You have 5 attempts.")
    entry_guess.config(state=tk.NORMAL)
    btn_check.config(state=tk.NORMAL)
    btn_start.config(state=tk.DISABLED)
    btn_reveal.config(state=tk.DISABLED)
    status_bar.config(text=f"Attempts left: {attempts_left}")
    lbl_guess_history.config(text="")
    lbl_mode.config(text=f"Current mode: {'Easy' if maximum_number == 50 else 'Hard'}")

def check_guess():
    global attempts_left, guess_history
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    
    if guess < minimum_number or guess > maximum_number:
        messagebox.showerror("Error", f"Please enter a number between {minimum_number} and {maximum_number}.")
        return
    
    guess_history.append(guess)
    lbl_guess_history.config(text=f"Your previous guesses: {guess_history}")
    attempts_left -= 1
    status_bar.config(text=f"Attempts left: {attempts_left}")
    
    if guess == secret_number:
        lbl_result.config(text=f"Congratulations! You guessed the number {secret_number} correctly.")
        entry_guess.config(state=tk.DISABLED)
        btn_check.config(state=tk.DISABLED)
        btn_start.config(state=tk.NORMAL)
        btn_reveal.config(state=tk.NORMAL)
    else:
        if attempts_left > 0:
            if guess < secret_number:
                lbl_result.config(text=f"Try again! Go higher.")
            else:
                lbl_result.config(text=f"Try again! Go lower.")
        else:
            lbl_result.config(text=f"Game over! The correct number was {secret_number}.")
            entry_guess.config(state=tk.DISABLED)
            btn_check.config(state=tk.DISABLED)
            btn_start.config(state=tk.NORMAL)
            btn_reveal.config(state=tk.NORMAL)

def show_instructions():
    messagebox.showinfo("Instructions", f"Try to guess a number between {minimum_number} and {maximum_number}. You have 5 attempts to guess correctly.")

def clear_guess_history():
    global guess_history
    guess_history = []
    lbl_guess_history.config(text="")

def reveal_number():
    lbl_result.config(text=f"The secret number was {secret_number}.")
    btn_reveal.config(state=tk.DISABLED)

def toggle_mode():
    global minimum_number, maximum_number
    if btn_toggle_mode.config('text')[-1] == 'Easy Mode':
        minimum_number, maximum_number = 1, 50
        btn_toggle_mode.config(text="Hard Mode")
    else:
        minimum_number, maximum_number = 1, 100
        btn_toggle_mode.config(text="Easy Mode")
    lbl_result.config(text=f"Mode switched! Try to guess a number between {minimum_number} and {maximum_number}. You have 5 attempts.")
    lbl_mode.config(text=f"Current mode: {'Easy' if maximum_number == 50 else 'Hard'}")
    start_game()

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

lbl_mode = tk.Label(root, text=f"Current mode: {'Easy' if maximum_number == 50 else 'Hard'}")
lbl_mode.pack(pady=5)

btn_toggle_mode = tk.Button(root, text="Hard Mode", command=toggle_mode)
btn_toggle_mode.pack(pady=5)

btn_reveal = tk.Button(root, text="Reveal Number", command=reveal_number, state=tk.DISABLED)
btn_reveal.pack(pady=5)

status_bar = tk.Label(root, text="Attempts left: 5", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
