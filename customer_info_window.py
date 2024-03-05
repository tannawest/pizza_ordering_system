"""
Program: Pizza Ordering System-Customer Information Window
Author: Tanna West
Date: 3/5/2024
Version: 1.0
Description: This program will allow our customer to input their name and address for pizza ordering.
"""

import tkinter as tk
from tkinter import messagebox

class CustomerInfoWindow(tk.Toplevel):
    def __init__(self, callback):
        super().__init__()
        self.title("Customer Information")
        self.geometry("300x150")
        self.callback = callback
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Address:").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        tk.Button(self, text="Submit", command=self.submit_info).pack()

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()

        if not name or not address:
            messagebox.showwarning("Error", "Please enter name and address.")
            return

        self.callback(name, address)
        self.destroy()

if __name__ == "__main__":
    app = CustomerInfoWindow()
    app.mainloop()
