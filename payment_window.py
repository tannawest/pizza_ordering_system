"""
Title: Pizza Ordering Payment
Author: Tanna West
Date: March 4, 2024
Version: 1.0
Description: This program adds up the total costs of the pizza order and allows the user to submit payment.
"""


class PizzaOrder:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self.calculate_price()

    def calculate_price(self):
        # Calculate price based on size and number of toppings
        base_price = 10  # Base price for a pizza
        size_prices = {"small": 0, "medium": 2, "large": 4}  # Price adjustment based on size
        topping_price = 1  # Price per topping

        total_price = base_price + size_prices[self.size] + (len(self.toppings) * topping_price)
        return total_price

def make_payment(amount_due):
    # Simulate payment process
    print("Payment due: $", amount_due)
    payment_amount = float(input("Enter payment amount: $"))
    if payment_amount >= amount_due:
        change = payment_amount - amount_due
        print("Thank you for your payment. Your change is: $", change)
        return True
    else:
        print("Insufficient payment. Payment failed.")
        return False

def main():
    # Example pizza order
    size = input("Enter pizza size (small, medium, large): ").lower()
    toppings = input("Enter toppings (comma-separated): ").split(",")

    order = PizzaOrder(size, toppings)
    print("Your total amount due is: $", order.price)

    # Process payment
    if make_payment(order.price):
        print("Your pizza order has been placed!")
    else:
        print("Payment failed. Please try again.")

if __name__ == "__main__":
    main()
