import tkinter as tk
from tkinter import messagebox
import random
import math

class NumberGuessingGame:
    def __init__(self, master, lower, upper):
        self.master = master
        self.master.title("Number Guessing Game")

        self.lower = lower
        self.upper = upper

        self.target_number = random.randint(lower, upper)
        self.max_chances = round(math.log(upper - lower + 1, 2))
        self.current_chances = 0

        self.label = tk.Label(master, text=f"You've only {self.max_chances} chances to guess the integer!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        self.current_chances += 1

        if guess == self.target_number:
            messagebox.showinfo("Congratulations", f"You did it in {self.current_chances} tries!")
            self.master.destroy()
        elif guess < self.target_number:
            messagebox.showinfo("Incorrect", "You guessed too small.")
        else:
            messagebox.showinfo("Incorrect", "You guessed too high.")

        if self.current_chances >= self.max_chances:
            messagebox.showinfo("Game Over", f"The number was {self.target_number}. Better Luck Next time.")
            self.master.destroy()

def main():
    lower_bound = int(input("Enter Lower bound:- "))
    upper_bound = int(input("Enter Upper bound:- "))

    root = tk.Tk()
    game = NumberGuessingGame(root, lower_bound, upper_bound)
    root.mainloop()

if __name__ == "__main__":
    main()
