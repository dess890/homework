# You are responsible for creating an app that manages groceries. 
# The app will support multiple Shopping Lists. Each shopping list will contain multiple items.

# Here are the features you need to implement:
# A user should be able to create shopping lists.
# A shopping list will have a name
# A user should be able to select a shopping list and then
# add items
# delete items
# view all items
# A user should be able to delete a shopping list
# A user should be able to view all shopping lists and their items:--
grocery_list = [{"Breakfast": "milk", "Lunch": "bread"}]
from createlist import create_list
from showlist import show_list
#menu function first
# grocery_list = {"Breakfast": "milk"}, {"Lunch": "bread"}

def menu():
    choices = input("""Pick either 1 or 2
    1. create a shopping list
    2. Access a shopping list""")
    if choices == "1":
        create_list()
    elif choices == "2":
        show_list()
    else:
        exit()

menu()

