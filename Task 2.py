# Complete the code to remove items from the fridge.


# Step 1: There are items already in the fridge and they have been saved to a list called fridge_items.


fridge_items = ["milk", "eggs", "butter", "cheese"]

while True:
    action = input("Enter 'remove' to remove an item: ").lower()

# Step 2: In the first if statement below, make action equal to 'remove.'

  
    if 
        item = input("Enter the item to remove: ").lower()

# Step 3: In the nested if statement below, check if the item is in the list fridge_items.
# Step 4: Add .remove(item) in line 22 to remove the item from the list.
  
        if 
            fridge_items
            print(f"{item} removed from the fridge.")
        else:
            print(f"{item} is not in the fridge.")
    else:
        print("Invalid action. Please enter 'remove'.")
