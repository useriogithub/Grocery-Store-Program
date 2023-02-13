
#Create Grocery Store class that has of departments
class GroceryStore:
    def __init__(self):
        self.departments = {"produce": {
             "oranges": 1.60,
            "romaine lettuce": 2.99,
            "pears": 3.99,
            "bananas": 0.99
            },
            "frozen": {
                "supreme pizza": 12.99,
                "Medley frozen veggie mix": 2.49,
                "Shredded Mozzerella Cheese": 1.45,
                "2% Milk": 5.88,
                "Heavy Whipping Cream": 6.99
                    },     
            "deli": {
                "ham": 2.99,
                "rotisserie chicken": 12.00,
                 "cobb salad": 2.99,
                 "cheddar cheese": 4.59
                   },
            "bakery": {
                "Blueberry Muffins": 5.99,
                "Whole Wheat Bread": 2.99,
                "Dinner Rolls": 2.56,
                "Chocolate Cake": 15.99,
                "Sourdough Loaf": 4.55,
                "Concerto Dessert": 6.99,
            },
            "Grocery": {
                "Stuffed Olives": 2.33,
                "Chex Mex Cereal": 2.20,
                "Ground Coffee Beans": 7.99,
                "Olive Oil": 4.89,
                "Ranch Dressing": 3.69,
                "Canned Green Beans": 2.88
            }
             
            }
        
    def display_departments(self):
        print("Here are the list of departments:")
        for department in self.departments:
            print(department)
            
    def display_items(self, department):
        if department in self.departments:
            print(f"Items in {department} department:")
            for item in self.departments[department]:
                print(f"{item} - {self.departments[department][item]}")
        else:
            print(f"{department} department does not exist.")
        
class ShoppingCart:
    def __init__(self): 
        self.items = {}
        self.prices = {}
        
    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        self.prices[item] = price

    def remove_item(self, item):
        if item in self.items:
            self.items[item] -= 1
        if self.items[item] <= 0:
            del self.items[item]
            del self.prices[item]
            
    def checkout(self):
        total = 0
        for item, price in self.prices.items():
            total += price
        return total
    
    def display_cart(self):
        if not self.items:
            print("your cart is empty.")
        else:
            for item, quantity in self.item.items():
                print(f'{item}: {quantity}')
                
store = GroceryStore()

cart = ShoppingCart()

                
while True:
    print('Welcome to our store!')
    print('1. Select department')
    print('2. view items in a department')
    print('3. Add item to cart')
    print('4. View cart')
    print('5. Exit')
    choice = input("Enter your choice: ")
    if choice == '1':
        store.display_departments()
    elif choice == '2':
        department = input("Enter the department name: ")
        store.display_items(department)       
        print('All done')
#this needs to go into the departments which display items

#second while loop?


        #chosen_department = input()
    elif choice == '3':
        department = input("Enter the department name: ")
        item = input("Enter the item name: ")
    
#item needs to be added from cart from choice 2


    elif choice == '4':
        store.display_cart(cart)
    else:
        print('Thank you for shopping with us!')
        break
        
        
        
        
        
