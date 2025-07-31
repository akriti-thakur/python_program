# first write pip install tk and
# pip install random in the terminal


import tkinter as tk
from tkinter import *
import random

# Initialize main window
win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks")

# Variables
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()
num = random.randint(1, 50)  # ✅ Secret number to guess

# Widgets
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

# Game logic
def fun():
    x = guess.get()
    current_score = score.get()

    if current_score > 0:
        if x < 1 or x > 50:
            hint.set("❌ Invalid guess! You just lost 1 chance.")
        elif x == num:
            hint.set("🎉 Congratulations, YOU WON!!!")
        elif x < num:
            hint.set("📉 Too low! Try a higher number.")
        else:
            hint.set("📈 Too high! Try a lower number.")
        score.set(current_score - 1)
        final_score.set(score.get())
    else:
        hint.set("💀 Game Over. You lost.")

# Button (after defining fun!)
Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

# Initial hints and scores
hint.set("🔍 Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

win.mainloop()