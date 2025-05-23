# List of vending machine items with names and prices
vending_items = {
    1: {"name": "Water", "price": 2.00},
    2: {"name": "Soda", "price": 3.50},
    3: {"name": "Chips", "price": 4.50},
    4: {"name": "Chocolate", "price": 6.00},
    5: {"name": "Coffee", "price": 7.50},
    6: {"name": "Juice", "price": 8.50},
    7: {"name": "Sandwich", "price": 9.00},
    8: {"name": "Energy Drink", "price": 10.00}
}

# Function to handle and validate money input
def get_valid_money_input():
    try:
        value = float(input("Insert money (RM0.5 or RM1 only): RM"))  # Get user input, convert to float
        if value == 0.5 or value == 1:   # Only accept RM0.5 or RM1
            return value
        else:
            return 'Invalid'  # Reject any other value (e.g. RM5, RM10, etc.)
    except ValueError:
        return 'Invalid'      # Reject input that is not a number

# NFA vending machine logic
def nfa_vending(selected_item):
    total_money = 0.0                          # Track total inserted money
    item_price = selected_item['price']        # Get selected item's price
    while True:
        inp = get_valid_money_input()          # Prompt user for money input
        if inp == 'Invalid':
            print("Invalid value inserted. Money not accepted, please continue.") # Ignore invalid input, don't reset money
        else:
            total_money += inp                # Add valid money to total
            print(f"Total inserted: RM{total_money:.2f}")
        if total_money == item_price:
            print(f"Exact amount received. Dispensing {selected_item['name']}.\n")
            break                             # Dispense item if exact amount
        elif total_money > item_price:
            change = total_money - item_price
            print(f"Dispensing {selected_item['name']}. Returning change: RM{change:.2f}\n")
            break                             # Dispense item and return change if more than price

# DFA vending machine logic
def dfa_vending(selected_item):
    total_money = 0.0                          # Track total inserted money
    item_price = selected_item['price']        # Get selected item's price
    while True:
        inp = get_valid_money_input()          # Prompt user for money input
        if inp == 'Invalid':
            print("Invalid value inserted! All input money returned. Start again from RM0.00.\n")
            total_money = 0.0                  # DFA: Reset money to zero on invalid input
            continue                          # Start over
        else:
            total_money += inp                # Add valid money to total
            print(f"Total inserted: RM{total_money:.2f}")
        if total_money == item_price:
            print(f"Exact amount received. Dispensing {selected_item['name']}.\n")
            break                             # Dispense item if exact amount
        elif total_money > item_price:
            change = total_money - item_price
            print(f"Dispensing {selected_item['name']}. Returning change: RM{change:.2f}\n")
            break                             # Dispense item and return change if more than price

# Main vending machine simulation
def vending_machine():
    while True:
        # Print vending machine banner and item list
        print("============================================")
        print("=== Welcome to the Happy Vending Machine ===")
        print("============================================")
        print("Item             Price (RM)")
        print("---------------------------")
        for key, item in vending_items.items():
            print(f"{key}. {item['name']:<15} RM{item['price']:.2f}")  # List all items

        try:
            item_num = int(input("\nEnter the number of item (0 to exit): "))  # Ask user to select item
        except ValueError:
            print("Invalid input. Please enter a valid item number.\n")
            continue

        if item_num == 0:                            # User can exit with 0
            print("Thank you for using the Happy Vending Machine!")
            break

        if item_num in vending_items:                # Check if item exists
            selected_item = vending_items[item_num]
            print(f"You selected: {selected_item['name']} - RM{selected_item['price']:.2f}")

            print("\n---------------------------")
            print("NFA [1]")
            print("DFA [2]")
            print("---------------------------")
            try:
                choice = int(input("\nNFA or DFA? Enter the number of choice: "))  # User selects NFA or DFA logic
            except ValueError:
                print("\nInvalid choice. Please enter 1 or 2.")
                continue

            if choice == 1:
                print("\nYou selected NFA.")
                nfa_vending(selected_item)       # Run NFA vending logic
            elif choice == 2:
                print("\nYou selected DFA.")
                dfa_vending(selected_item)       # Run DFA vending logic
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        else:
            print("\nInvalid item number.\n")    # Handle invalid item number

# Start the program
vending_machine()
