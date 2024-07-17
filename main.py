import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = 5
    lbl_result.config(text="New game started! Guess a number between 1 and 100. You have 5 attempts.")
    entry_guess.config(state=tk.NORMAL)
    btn_check.config(state=tk.NORMAL)
    btn_start.config(state=tk.DISABLED)

def check_guess():
    global attempts_left
    guess = int(entry_guess.get())
    attempts_left -= 1
    if guess == secret_number:
        lbl_result.config(text=f"Congratulations! You guessed the number {secret_number} correctly.")
        entry_guess.config(state=tk.DISABLED)
        btn_check.config(state=tk.DISABLED)
        btn_start.config(state=tk.NORMAL)
    else:
        if attempts_left > 0:
            if guess < secret_number:
                lbl_result.config(text=f"Try again! Guess higher. Attempts left: {attempts_left}")
            else:
                lbl_result.config(text=f"Try again! Guess lower. Attempts left: {attempts_left}")
        else:
            lbl_result.config(text=f"Game over! The correct number was {secret_number}.")
            entry_guess.config(state=tk.DISABLED)
            btn_check.config(state=tk.DISABLED)
            btn_start.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Number Guessing Game")

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

root.mainloop()
