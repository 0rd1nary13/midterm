# This program is written by team: Stack under flow
# Feb 9th, 2024


class FoodItems:
    def __init__(self, name, price, item_id, quantity):
        self.quantity = quantity
        self.name = name
        self.price = price
        self.id = item_id

    def display(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Number of selection: ", self.id)

    def item_total(self):
        return self.price * self.quantity


class FoodCourt:
    def __init__(self, name, foodItems):
        self.name = name
        self.foodItems = foodItems

    def show_menu(self):
        print("Welcome to ", self.name)
        for foodItem in self.foodItems:
            foodItem.display()


class Customer:
    def __init__(self, is_student, foodItems):
        self.is_student = False
        self.foodItems = foodItems

    def check_student(self):
        print("Are you a student? (y/n)")
        choice = input()
        if choice == 'y':
            self.is_student = True
        else:
            self.is_student = False

    def print_bill(self):
        total = 0
        # Print what the customer ordered
        print("Bill")
        try:
            for foodItem in self.foodItems:
                print(foodItem.name, " ", foodItem.price, " ", foodItem.quantity, " ", foodItem.item_total())
                total += foodItem.item_total()
        except:
            print("No items ordered, thank you for using our service.")
        if not self.is_student:
            total = total * 1.09
        print("Total: ", round(total, 2))

    def get_input(self):
        foodItems = []
        while True:
            print("Enter the food item number: ")
            print("Enter 6 to exit.")
            item_id = int(input())
            if item_id == 6:
                break
            print("Enter the quantity: ")
            quantity = int(input())
            for foodItem in self.foodItems:
                if foodItem.id == item_id:
                    foodItem.quantity = quantity
                    foodItems.append(foodItem)
            print("Do you want to add more items? (y/n)")
            choice = input()
            if choice == 'n':
                break
        return foodItems


def main():
    DeAnza = FoodCourt("De Anza Food Court",
                       [FoodItems("De Anza Burger", 5.25, 1, 0),
                        FoodItems("Bacon Cheese", 5.75, 2, 0),
                        FoodItems("Mushroom Swiss", 5.95, 3, 0),
                        FoodItems("Western Burger", 5.95, 4, 0),
                        FoodItems("Don Cali Burger", 5.95, 5, 0), ])
    DeAnza.show_menu()
    customer = Customer(False, DeAnza.foodItems)
    customer.check_student()
    customer.foodItems = customer.get_input()
    customer.print_bill()


main()


'''
import time
import datetime

from person import Student
from person import Staff
from burgers import DeAnzaBurger
from burgers import BaconCheese
from burgers import MushroomSwiss
from burgers import WesternBurger
from burgers import DonCaliBurger
   
class Order:
    def __init__(self):
        # "_" means they are private
        self._price_no_tax = 0
        self._price_after_tax = 0
        self._total_tax = 0
        self.name = "De Anza Food Court"

        self._menu_items = {
            "De Anza Burger": 5.25,
            "Bacon Cheese": 5.75,
            "Mushroom Swiss": 5.95,
            "Western Burger": 5.95,
            "Don Cali Burger": 5.95
        }

        self._order_dict = {key: 0 for key in self._menu_items}
    
    # Implement CRUD
    def create(self, key, value):
        self._menu_items[key] = value

    def read(self):
        for key, value in self._menu_items.items():
            print(key, ": ", value)

    def delete(self, key):
        del self._menu_items[key]

    def update(self, key, value):
        self._menu_items[key] = value

    def display_menu(self):
        print("            Welcome to", self.name)
        print("**********************************************************")
        menu_keys = list(self._menu_items.keys())
        for item_name, price in self._menu_items.items():
            print(f"{item_name:<30} ${price:>5.2f}")
        print("**********************************************************")
        print("Enter '6' to exit")

    def get_input(self):
        menu_keys = list(self._menu_items.keys())
        while True:
            user_input = input("Enter the name of the burger you'd like to order, Enter 6 to exit: ").strip()
            if user_input == '6':
                print("Thank you, hope to see you again!")
                break
  
            try:
                item_index = int(user_input) - 1  # Convert to zero-based index
                if 0 <= item_index < len(menu_keys):
                    item_name = menu_keys[item_index]
                    quantity = int(input(f"Enter the quantity for {item_name}: ").strip())
                    if quantity < 0:
                        raise ValueError("Quantity cannot be negative.")
                    self._order_dict[item_name] += quantity
                else:
                    print("Please enter a valid menu item number.")
            except ValueError as e:
                print(f"Invalid input: {e}")

    def calculate(self):
        customer_type = input("Is the customer a Student ? (y/n): ").strip().lower()
        if customer_type == 'y':
            self._tax_rate = 0
        else:
            self._tax_rate = 0.09

        self._price_no_tax = sum(self._order_dict[item] * self._menu_items[item] for item in self._order_dict)
        self._total_tax = self._price_no_tax * self._tax_rate
        self._price_after_tax = self._price_no_tax + self._total_tax
        
    def print_bill(self):
        print("Here is your cost detail")
        print("**********************************************************")
        for item_name, quantity in self._order_dict.items():
            if quantity > 0:
                item_price = self._menu_items[item_name]
                item_cost = item_price * quantity
                print(f"{item_name} - Price: ${item_price}, Quantity: {quantity}, Cost: ${item_cost}")
        print("**********************************************************")
        print("The total before tax: ", round(self._price_no_tax, 2))
        print("Tax Amount: ", round(self._total_tax, 2))
        print("Total price after tax: ", round(self._price_after_tax, 2))
        
    def save_to_file(self):
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
        filename = order_time_stamp + '.txt'

        with open(filename, 'w') as file:
            file.write("            Here is your order detail:\n")
            file.write("**********************************************************\n")
            for item_name, quantity in self._order_dict.items():
                if quantity > 0:
                    item_price = self._menu_items[item_name]
                    item_cost = item_price * quantity
                    file.write(f"{item_name} - Price: ${item_price:.2f}, Quantity: {quantity}, Cost: ${item_cost:.2f}\n")
            file.write("**********************************************************\n")
            file.write(f"Total before tax: ${self._price_no_tax:.2f}\n")
            file.write(f"Tax Amount: ${self._total_tax:.2f}\n")
            file.write(f"Total price after tax: ${self._price_after_tax:.2f}\n")

from Order import Order
from person import Student, Staff
from burgers import DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, DonCaliBurger

def main():
    flag = True

    while flag:
        order = Order()
        order.display_menu()
        order.get_input()  # Note the correction to match the method name
        order.calculate()
        order.print_bill()
        order.save_to_file()
        
        user_input_to_continue = input("Continue for another order (Any key=Yes, n=No)? ").strip().lower()

        if user_input_to_continue == 'n':
            print("The system is shutting down!")
            flag = False

if __name__ == "__main__":
    main()

class Student:
    def __init__(self):
        super().__init__()
        self.tax_rate = 0 
    def get_tax_rate(self):
        return self.tax_rate

class Staff:
    def __init__(self):
        super().__init__()
        self.tax_rate = 0.09
    def get_tax_rate(self):
        return self.tax_rate

class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price}")

class DeAnzaBurger(Burger):
    def __init__(self):
        super().__init__("De Anza Burger", 5.25)

class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 5.75)

class MushroomSwiss(Burger):
    def __init__(self):
        super().__init__("Mushroom Swiss", 5.95)

class WesternBurger(Burger):
    def __init__(self):
        super().__init__("Western Burger", 5.95)

class DonCaliBurger(Burger):
    def __init__(self):
        super().__init__("Don Cali Burger", 5.95)

'''
