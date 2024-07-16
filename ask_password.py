#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

def submit_password(event=None):
    password = password_entry.get()
    print(password)
    master.destroy()

def center_window(master, width=300, height=100):
    # Get the screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window size and position
    master.geometry(f'{width}x{height}+{x}+{y}')

def main():
    global master
    master = Tk()
    master.title("Password Entry")
    master.geometry("400x70")

    center_window(master)

    label = Label(master)
    label.grid(row=0, column=0, padx=10, pady=10)

    global password_entry
    password_entry = Entry(master, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.focus()
    password_entry.bind("<Return>", submit_password)

    submit_button = Button(master, text="OK", command=submit_password)
    submit_button.grid(row=0, column=2, padx=10, pady=10)

    master.mainloop()

if __name__ == "__main__":
    main()