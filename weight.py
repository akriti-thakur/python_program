import tkinter as tk
from tkinter import *

# Create the window
window = Tk()
window.title("PythonGeeks")
window.geometry("500x500")

# Define variable
kg = DoubleVar()

# Function to convert to grams
def convert_to_gram():
    kg_val = kg.get()
    gram = float(kg_val) * 1000
    Label(window, text="This weight in grams would be", font=("Arial", 12)).pack()
    Label(window, text=gram, bg="red").pack()

# Function to convert to ounces
def convert_to_ounce():
    kg_val = kg.get()
    ounce = float(kg_val) * 35.274
    Label(window, text="This weight in ounce would be", font=("Arial", 12)).pack()
    Label(window, text=ounce, bg="red").pack()

# Function to convert to pounds
def convert_to_pound():
    kg_val = kg.get()
    pound = float(kg_val) * 2.20462
    Label(window, text="This weight in pound would be", font=("Arial", 12)).pack()
    Label(window, text=pound, bg="red").pack()

# UI Layout
Label(window, text="WEIGHT CONVERTER", font=("Arial", 20), bg="black", fg='yellow').pack()
Label(window, text="Enter the weight in Kgs", font=("Arial", 14)).pack()
Entry(window, textvariable=kg).pack()

Button(window, text="Convert to Gram", bg="blue", command=convert_to_gram).pack()
Button(window, text="Convert to Ounce", bg="blue", command=convert_to_ounce).pack()
Button(window, text="Convert to Pound", bg="blue", command=convert_to_pound).pack()

window.mainloop()