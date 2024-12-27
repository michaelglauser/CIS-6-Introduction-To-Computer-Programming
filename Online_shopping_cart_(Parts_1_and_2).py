
# 9.11 LAB*: Program: Online shopping cart (Part 1)

# (1) Build the ItemToPurchase class with the following specifications:

#     Attributes (3 pts)
#         item_name (string)
#         item_price (float)
#         item_quantity (int)
#     Default constructor (1 pt)
#         Initializes item's name = "none", item's price = 0, item's quantity = 0
#     Method
#         print_item_cost()


# Ex. of print_item_cost() output:

# Bottled Water 10 @ $1 = $10

# (2) In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class. (2 pts)

# Ex:

# Item 1
# Enter the item name:
# Chocolate Chips
# Enter the item price:
# 3
# Enter the item quantity:
# 1

# Item 2
# Enter the item name:
# Bottled Water
# Enter the item price:
# 1
# Enter the item quantity:
# 10


# (3) Add the costs of the two items together and output the total cost. (2 pts)

# Ex:

# TOTAL COST
# Chocolate Chips 1 @ $3 = $3
# Bottled Water 10 @ $1 = $10

# Total: $13


# 9.12 LAB*: Program: Online shopping cart (Part 2)

# This program extends the earlier "Online shopping cart (Part 1)" program. (Consider first saving your earlier program).
# Step 1: Extend the ItemToPurchase class to contain a new attribute. (2 pts)

#     item_description (string) - Initalized in default constructor to "none"

# Implement the following method for the ItemToPurchase class.

#     print_item_description() - Prints item_description attribute for an ItemToPurchase object.

# Ex. of print_item_description() output:

# Bottled Water: Deer Park, 12 oz.

# Step 2: Build the ShoppingCart class with the following data attributes and related methods.

#     Parameterized constructor which takes the customer name and date as parameters (2 pts)
#     Attributes
#         customer_name (string) - Initialized in default constructor to "none"
#         current_date (string) - Initialized in default constructor to "January 1, 2016"
#         cart_items (list)
#     Methods
#         add_item()
#             Adds an item to cart_items list. Has a parameter of type ItemToPurchase. Does not return anything.
#         remove_item()
#             Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
#             If item name cannot be found, output a message: Item not found in cart. Nothing removed.
#         modify_item()
#             Modifies an item's quantity. Has a parameter of type ItemToPurchase. Does not return anything.
#             If item can be found (by name) in cart, modify item in cart.
#             If item cannot be found (by name) in cart, output a message: Item not found in cart. Nothing modified.
#         get_num_items_in_cart() (2 pts)
#             Returns quantity of all items in cart. Has no parameters.
#         get_cost_of_cart() (2 pts)
#             Determines and returns the total cost of items in cart. Has no parameters.
#         print_total()
#             Outputs total of objects in cart.
#             If cart is empty, output a message: SHOPPING CART IS EMPTY
#         print_descriptions()
#             Outputs each item's description.
#             If cart is empty, output a message: SHOPPING CART IS EMPTY

# Ex. of print_total() output:

# John Doe's Shopping Cart - February 1, 2016
# Number of Items: 8

# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128

# Total: $521

# Ex. of print_descriptions() output:

# John Doe's Shopping Cart - February 1, 2016

# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones

# Step 3: In the main section of the code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart. (1 pt)

# Ex:

# Enter customer's name:
# John Doe
# Enter today's date:
# February 1, 2016

# Customer name: John Doe
# Today's date: February 1, 2016

# Step 4: Implement the following menu functions

#     print_menu()
#         Prints the following menu of options to manipulate the shopping cart. (1 pt)

# MENU
# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit

#     execute_menu()
#         Takes 2 parameters: a character representing the user's choice and a shopping cart. Performs the menu options described below in step 5, according to the user's choice. (1 pt)

# Step 5: Implement the menu options

# Step 5a: In the main section of the code, call print_menu() and prompt for the user's choice of menu options. Each option is represented by a single character.

# If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute the option by calling execute_menu(). Then, print the menu and prompt for a new option. Continue until the user enters 'q'. (1 pt)

# Hint: Implement Quit before implementing other options.

# Ex:

# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit

# Choose an option:

# Step 5b: Implement "Output shopping cart" menu option in execute_menu(). (3 pts)

# Ex:

# OUTPUT SHOPPING CART
# John Doe's Shopping Cart - February 1, 2016
# Number of Items: 8

# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128

# Total: $521

# Step 5c: Implement "Output items' descriptions" menu option in execute_menu(). (2 pts)

# Ex:

# OUTPUT ITEMS' DESCRIPTIONS
# John Doe's Shopping Cart - February 1, 2016

# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones

# Step 5d: Implement "Add item to cart" menu option in execute_menu(). (3 pts)

# Ex:

# ADD ITEM TO CART
# Enter the item name:
# Nike Romaleos
# Enter the item description:
# Volt color, Weightlifting shoes
# Enter the item price:
# 189
# Enter the item quantity:
# 2

# Step 5e: Implement "Remove item from cart" menu option in execute_menu(). (4 pts)

# Ex:

# REMOVE ITEM FROM CART
# Enter name of item to remove:
# Chocolate Chips

# Step 5f: Implement "Change item quantity" menu option in execute_menu(). (5 pts)

# Hint: Make a new ItemToPurchase object before using ModifyItem() method.

# Ex:

# CHANGE ITEM QUANTITY
# Enter the item name:
# Nike Romaleos
# Enter the new quantity:
# 3



class ItemToPurchase:

  def __init__(self,
               item_name="none",
               item_price=0,
               item_quantity=0,
               item_description="none"):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  # prints out the item cost
  def print_item_cost(self):
    self.item_price = int(self.item_price)
    self.item_quantity = int(self.item_quantity)
    return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price*self.item_quantity}'

  # prints item_description attribute  for an itemToPurchase object
  def print_item_description(self):
    return f'{self.item_name}: {self.item_description}'


class ShoppingCart(ItemToPurchase):

  def __init__(self, customer_name, current_date):
    ItemToPurchase.__init__(self)
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  # adds an item to cart_items
  def add_item(self, obj):
    self.cart_items.append(obj)

  # remove items from the cart
  def remove_item(self, item):
    count = 0
    for i in range(len(self.cart_items) - 1):
      if self.cart_items[i].item_name == item:
        self.cart_items.pop(i)
        count += 1
        break
    if count == 0:
      print("Item not found in cart. Nothing removed.")

  # modify item in cart by the name
  def modify_item(self, obj):
    for cart_item in self.cart_items:
      if cart_item.item_name == obj.item_name:
        cart_item.item_quantity = obj.item_quantity
    else:
      print("Item not found in cart. Nothing modified.")

  # returns the number of item in the list
  def get_num_items_in_cart(self):
    total_quantity = 0
    for x in self.cart_items:
      self.item_quantity = int(x.item_quantity)
      total_quantity += self.item_quantity
    return total_quantity

  # returns the total cost of items
  def get_cost_of_cart(self):
    cart_cost = 0
    for i in self.cart_items:
      self.item_price = int(i.item_price)
      self.item_quantity = int(i.item_quantity)
      cost = self.item_price * self.item_quantity
      cart_cost += cost
    return cart_cost

  # outputs total objects in cart
  def print_total(self):
    if len(self.cart_items) == 0:
      print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
      print(f'Number of Items: {self.get_num_items_in_cart()}\n')
      print("SHOPPING CART IS EMPTY\n")
      print(f'Total: ${self.get_cost_of_cart()}')
    else:
      print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
      print(f'Number of Items: {self.get_num_items_in_cart()}\n')
      for item in self.cart_items:
        print(item.print_item_cost())
      print()
      print(f'Total: ${self.get_cost_of_cart()}')

  # outputs the name of the item and description
  def print_descriptions(self):
    print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
    print()
    print("Item Descriptions")
    for item in self.cart_items:
      print(item.print_item_description())

# menu
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
  


# excute menu
def execute_menu(char, cart):
  if char == "a":
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_desc = input("Enter the item description:\n")
    item_price = input("Enter the item price:\n")
    item_quantity = input("Enter the item quantity:\n")
    item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
    cart.add_item(item)
    
  elif char == "r":
    print("REMOVE ITEM FROM CART")
    rmv_item = input("Enter name of item to remove:\n")
    cart.remove_item(rmv_item)
    
  elif char == "c":
    print("CHANGE ITEM QUANTITY")
    item_name = input("Enter the item name:\n")
    new_qunatity = input("Enter the new quantity:\n")
    new_obj = ItemToPurchase(item_name, sc.item_price, new_qunatity,
                             sc.item_description)
    cart.modify_item(new_obj)
    
  elif char == "i":
    print("OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_descriptions()
  elif char == "o":
    print("OUTPUT SHOPPING CART")
    cart.print_total()


if __name__ == "__main__":
  choice = ""
  options = ["a", "r", "c", "i", "o", "q"]
  # parameters for ShoppingCart
  custo_name = input("Enter customer's name:\n")
  today_date = input("Enter today's date:\n")
  print()
  sc = ShoppingCart(custo_name, today_date)
  print(f'Customer name: {sc.customer_name}')
  print(f"Today's date: {sc.current_date}\n")
  print_menu()
  print()
  # while loop that prints the menu until user enters q - quit
  while True:
    
    choice = input("Choose an option:\n")
    if choice == "q":
      break
    else:
      if choice in options:
        execute_menu(choice, sc)
        print()
        print_menu()
        print()
      else:
        choice = input("Choose an option:\n")