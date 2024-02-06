"""
from tkinter import *
import socket
import threading

root = Tk()
root.config(bg="black")
root.geometry("1366x768")
root.title("Socket Test")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='black')





canvas.pack()
root.mainloop()
"""
import tkinter as tk

def on_submit():
    # Function to be called when the entry is submitted
    entry_value = entry.get()
    print("Submitted:", entry_value)

root = tk.Tk()
root.config(bg='black')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Create a Frame widget covering the entire screen
frame = tk.Frame(root, width=screen_width, height=screen_height, bg='blue')
frame.pack(expand=True, fill='both')

# Create a Text widget
text_widget = tk.Text(frame, wrap=tk.WORD, bg='black')
text_widget.pack(expand=True, fill='both')

# Create an Entry widget
entry = tk.Entry(frame, bg='black')
entry.pack(side='bottom', fill='x')

# Create a button to submit the entry
submit_button = tk.Button(frame, text="Submit", command=on_submit, bg='black')
submit_button.pack(side='bottom')

root.mainloop()
