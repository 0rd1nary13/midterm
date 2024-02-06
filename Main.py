# This program is written by team: Stack under flow
# Feb 5th, 2024


class FoodItems:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id

    def display(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Number of selection: ", self.id)


class FoodCourt:
    def __init__(self, name, foodItems):
        self.name = name
        self.foodItems = foodItems

    def show_menu(self):
        print("Food Court Name: ", self.name)
        for foodItem in self.foodItems:
            foodItem.display()
            print("")

    def get_input(self):
        foodItems = []
        while True:
            print("Enter the food item number: ")
            id = int(input())
            print("Enter the quantity: ")
            quantity = int(input())
            foodItems.append(FoodItems(self.foodItems[id-1].name, self.foodItems[id-1].price, quantity))
            print("Do you want to add more items? (y/n)")
            choice = input()
            if choice == 'n':
                break
        return foodItems

   def compute_bill(self, foodItems):
        total = 0
        for foodItem in foodItems:
            total += foodItem.price*foodItem.id
        return total

    def print_bill(self, foodItems):
        print("Food Court Name: ", self.name)
        for foodItem in foodItems:
            foodItem.display()
            print("")
        print("Total Bill: ", FoodCourt.compute_bill(self, foodItems))
def main():
    DeAnza = FoodCourt("De Anza Food Court",
              [FoodItems("De Anza Burger", 5.25, 1),
               FoodItems("Bacon Cheese", 5.75, 2),
               FoodItems("Mushroom Swiss", 5.95, 3),
               FoodItems("Western Burger", 5.95, 4),
               FoodItems("Don Cali Burger", 5.95, 5), ])
    #display the menu
    FoodCourt.show_menu(DeAnza)
    #get the input from the user
    foodItems = FoodCourt.get_input(DeAnza)
    #print the bill
    FoodCourt.print_bill(DeAnza, foodItems)


main()