import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Information", "Button was clicked!")
    print("Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("Click Event Example")

# Create a button and attach the click event handler
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()
