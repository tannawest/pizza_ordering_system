"""
Program: Pizza Ordering System-Pizza Ordering Window
Author: Tanna West
Date: 3/5/2024
Version: 1.0
Description: This window allows the customer to select their pizza and toppings.
"""

import tkinter as tk
from tkinter import messagebox
from customer_info_window import CustomerInfoWindow
from pizza_price_calculator import PizzaPriceCalculator

class OrderSummaryWindow(tk.Toplevel):
    def __init__(self, parent, customer_info, size, toppings, toppings_image, pizza_image):
        super().__init__(parent)
        self.title("Order Summary")
        self.geometry("500x400")  # Increased height to accommodate the image
        self.customer_info = customer_info
        self.size = size
        self.toppings = toppings
        self.toppings_image = toppings_image
        self.pizza_image = pizza_image
        self.price_calculator = PizzaPriceCalculator()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Order Summary:").pack()

        order_details = f"Name: {self.customer_info['name']}\n"
        order_details += f"Address: {self.customer_info['address']}\n"
        order_details += f"Pizza Size: {self.size}\n"
        order_details += f"Toppings: {', '.join(self.toppings)}\n"
        total_price = self.price_calculator.calculate_price(self.size, self.toppings)
        order_details += f"Total Price: ${total_price:.2f}\n"
        tk.Label(self, text=order_details).pack()

        tk.Label(self, image=self.toppings_image).pack()

        tk.Label(self, image=self.pizza_image).pack()

        tk.Button(self, text="Submit Order", command=self.submit_order).pack()

    def submit_order(self):
        # Here you would process the order
        messagebox.showinfo("Order Submitted", "Your order has been submitted!")
        self.destroy()

class PizzaOrderingSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pizza Ordering System")
        self.geometry("400x200")
        self.customer_info = {"name": "", "address": ""}
        self.create_widgets()
        self.price_calculator = PizzaPriceCalculator()

    def create_widgets(self):
        tk.Label(self, text="Pizza Size:").pack()

        # Options for pizza size
        self.size_var = tk.StringVar()
        self.size_var.set("Select Size")
        self.size_options = ["Small", "Medium", "Large"]
        self.size_menu = tk.OptionMenu(self, self.size_var, *self.size_options)
        self.size_menu.pack()

        tk.Label(self, text="Toppings:").pack()

        # Options for toppings
        self.toppings_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, height=5)
        for topping in ["Pepperoni", "Mushrooms", "Onions", "Peppers", "Sausage"]:
            self.toppings_listbox.insert(tk.END, topping)
        self.toppings_listbox.pack()

        tk.Button(self, text="Get Price", command=self.show_order_summary).pack()

    def get_customer_info(self, name, address):
        self.customer_info["name"] = name
        self.customer_info["address"] = address
        self.show_order_summary()  # Show toppings window after getting customer info

    def show_order_summary(self):
        size = self.size_var.get()
        selected_toppings = self.toppings_listbox.curselection()

        if size == "Select Size" or not selected_toppings or not self.customer_info["name"] or not self.customer_info["address"]:
            messagebox.showwarning("Error", "Please select a size, at least one topping, and provide your name and address.")
            return

        toppings = [self.toppings_listbox.get(index) for index in selected_toppings]

        # Load image for toppings
        toppings_image = tk.PhotoImage(file="toppings_photo.png")

        # Load image for pizza
        pizza_image = tk.PhotoImage(file="pizza_photo.png")

        order_summary_window = OrderSummaryWindow(self, self.customer_info, size, toppings, toppings_image, pizza_image)

if __name__ == "__main__":
    app = PizzaOrderingSystem()
    customer_info_window = CustomerInfoWindow(app.get_customer_info)
    customer_info_window.mainloop()
