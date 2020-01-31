def main_menu():
    print("1. Adjust incomplete items")
    print("2. Adjust completed items")
    print("3. Show all items")
    print("4. Add new item")
    print("5. Delete items")
    print("6. Exit")
    return input("Pick one")

def show_item(item):
    print(item)

def select_item():
    return input("Select the item you want to change\n")

def change_status():
    return input("Do you want to change it to complete? [Y/N]")

def add():
    title = input("What's the to do?")
    descrip = input("Describe the to do")
    complete = input("Have you done this already?")
    return title, descrip, complete

def enter_to_continue():
    input("Press Enter to continue")

def delete_one():
    return input("Choose one to delete\n")
    
def goodbye():
    print("Peace out")

#Bad inputs
def bad_input():
    print("That shit won't fly")