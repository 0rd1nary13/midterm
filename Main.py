# This program is written by team: Stack under flow
# Feb 5th, 2024


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
        print("Total: ", total)

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
