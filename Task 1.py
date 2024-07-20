#Your first task is to add items to the list when the Samsung fridge detects that it has been added to the fridge.

# Step 1: An empty list of fridge items has been set up for you and a while True loop. In the variable 'action,' ask for user input through "Enter 'add' to add an item: "   Also add .lower() to the end.

fridge_items = []

while True:
    action = 


# Step 2: Use an if statement which says if the action is equal to 'add'
  
    if action == 'add':
        item = input("Enter the item to add: ").lower()

        print(f"{item} added to the fridge.")  
    else:
        print("Invalid action. Please enter 'add'.")


# Step 3: Underneath the above 'if' statement where the gap is on line 15, write a line of code using 'append' to add an item to the list of fridge_items.
