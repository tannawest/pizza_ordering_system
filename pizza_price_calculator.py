"""
Program: Pizza Price Calculator - Pizza Ordering System
Author: Tanna West
Date: 3/5/2024
Version: 1.0
Description: This program determines the price of the order for our pizza ordering system.
"""

class PizzaPriceCalculator:
    def __init__(self):
        self.size_prices = {"Small": 8.99, "Medium": 10.99, "Large": 12.99}
        self.topping_prices = {"Pepperoni": 1.50, "Mushrooms": 1.00, "Onions": 0.75, "Peppers": 0.75, "Sausage": 1.50}

    def calculate_price(self, size, toppings):
        size_price = self.size_prices.get(size, 0)
        toppings_price = sum([self.topping_prices.get(topping, 0) for topping in toppings])
        total_price = size_price + toppings_price
        return total_price


