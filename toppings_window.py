"""
Title: Pizza Ordering System
Author: Tanna West
Date: 2/20/2024
Version: 1.0
Description: This program is the toppings module for our pizza ordering system.
"""

import tkinter as tk
from PIL import ImageTk, Image

class ToppingsWindow:
    def __init__(self, master):
        self.master = master
        self.toppings_window = tk.Toplevel(master)
        self.toppings_window.title("Select Toppings")

        # Load image
        pizza_img = Image.open("pizza_toppings.png")
        pizza_img = pizza_img.resize((200, 200), Image.ANTIALIAS)  # Resize the image if needed
        self.img = ImageTk.PhotoImage(pizza_img)

        # Display image
        self.img_label = tk.Label(self.toppings_window, image=self.img)
        self.img_label.pack()

        # List of available toppings
        self.available_toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra Cheese"]

        # Create checkboxes for each topping
        self.selected_toppings = []
        for topping in self.available_toppings:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.toppings_window, text=topping, variable=var)
            checkbox.pack(anchor=tk.W)
            self.selected_toppings.append((topping, var))

        # Submit button
        self.submit_button = tk.Button(self.toppings_window, text="Submit", command=self.submit_toppings)
        self.submit_button.pack()

    def submit_toppings(self):
        # Retrieve selected toppings
        selected = [topping for topping, var in self.selected_toppings if var.get()]

        # Process selected toppings (e.g., calculate price, update order)
        # For now, let's just print them
        print("Selected Toppings:", selected)

# Example usage
root = tk.Tk()
app = ToppingsWindow(root)
root.mainloop()
