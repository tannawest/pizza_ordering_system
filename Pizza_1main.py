"""
Title: Pizza Ordering System
Author: Tanna West
Date: 2/20/2024
Version: 1.0
Description: This program is the main application for our pizza ordering system,
"""

import tkinter as tk
import delivery_window
import toppings_window

class PizzaOrderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizza Ordering System")

        self.label = tk.Label(master, text="Welcome to Pizza Ordering System")
        self.label.pack()

        self.order_button = tk.Button(master, text="Place Order", command=self.open_delivery_window)
        self.order_button.pack()

        self.select_toppings_button = tk.Button(master, text="Select Toppings", command=self.open_toppings_window)
        self.select_toppings_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack()

    def open_delivery_window(self):
        delivery_window.DeliveryWindow(self.master)

    def open_toppings_window(self):
        toppings_window.ToppingsWindow(self.master)

    def exit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
