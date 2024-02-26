"""
Title: Pizza Ordering System
Author: Tanna West
Date: 2/25/2024
Version: 1.0
Description: This program is the delivery window module for our pizza ordering system,
"""

import tkinter as tk

class DeliveryWindow:
    def __init__(self, master):
        self.master = master
        self.delivery_window = tk.Toplevel(master)
        self.delivery_window.title("Delivery Details")

        # Create and place widgets for entering delivery details
        self.label_name = tk.Label(self.delivery_window, text="Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.delivery_window)
        self.entry_name.pack()

        self.label_address = tk.Label(self.delivery_window, text="Address:")
        self.label_address.pack()

        self.entry_address = tk.Entry(self.delivery_window)
        self.entry_address.pack()

        self.submit_button = tk.Button(self.delivery_window, text="Submit", command=self.submit_delivery_details)
        self.submit_button.pack()

    def submit_delivery_details(self):
        # Retrieve delivery details from entry fields
        name = self.entry_name.get()
        address = self.entry_address.get()

        # Process delivery details (e.g., save to database, etc.)
        # For now, let's just print them
        print("Delivery Details:")
        print("Name:", name)
        print("Address:", address)
