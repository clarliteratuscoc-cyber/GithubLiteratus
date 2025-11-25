# Simple Budget Allocation Planner System
print("Welcome to the Simple Budget Allocation Planner System!")

# Get user's total budget
total_budget = float(input("Enter your total budget for the week: "))

# Initialize variables
expenses = []
expense_types = []
expense_days = []  
total_expenses = 0

while True:
    print("\nMenu:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View remaining budget")
    print("4. View expenses by day")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        day = input("Enter the day of the week (e.g., Monday): ")

        remaining = total_budget - total_expenses
        if remaining <= 0:
            print("You don't have enough money to add new expenses!")
            break

        expense_name = input("Enter expense name (e.g., Food, Tour, School): ")
        expense_amount = float(input("Enter expense amount: "))

        if expense_amount > remaining:
            print(f"Not enough budget! You only have ₱{remaining:.2f} left.")
            break
        
        expenses.append(expense_amount)
        expense_types.append(expense_name)
        expense_days.append(day)

        total_expenses += expense_amount
        print(f"Added {expense_name} expense of ₱{expense_amount:.2f} on {day}.")

        if total_budget - total_expenses <= 0:
            print("Your budget is now ₱0.00.")
    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            for i in range(len(expenses)):
                print(f"{expense_types[i]} - ₱{expenses[i]:.2f} (Day: {expense_days[i]})")
            print(f"Total expenses: ₱{total_expenses:.2f}")
    
    elif choice == "3":
        remaining = total_budget - total_expenses
        print(f"Remaining budget: ₱{remaining:.2f}")
    
    elif choice == "4":
        day_search = input("Enter the day to view expenses: ")
        print(f"\nExpenses for {day_search}:")
        found = False
        day_total = 0

        for i in range(len(expenses)):
            if expense_days[i].lower() == day_search.lower():
                print(f"{expense_types[i]} - ₱{expenses[i]:.2f}")
                found = True
                day_total += expenses[i]

        if not found:
            print("No expenses found for that day.")
        else:
            print(f"Total spent on {day_search}: ₱{day_total:.2f}")

    elif choice == "5":
        print("Exiting the Budget Planner. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")