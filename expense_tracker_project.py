# EXENSE TRACKER PROJECT

# Create file if not exists
def initialize_file():
    try:
        open("expenses.txt", "x")
    except FileExistsError:
        pass


# 1. Add an expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food/Travel/Bills/etc): ")
    note = input("Enter note/description: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("✔ Expense added successfully!\n")


# 2. View all expenses
def view_expenses():
    print("\n===== All Expenses =====")

    try:
        with open("expenses.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No expenses recorded yet.\n")
                return

            for line in data:
                amount, category, note = line.strip().split(",")
                print(f"Amount: ₹{amount} | Category: {category} | Note: {note}")

    except FileNotFoundError:
        print("No expense file found.\n")

    print()


# 3. Total of all expenses
def total_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount = line.split(",")[0]
                total += float(amount)

        print(f"\n Total Expenses = ₹{total}\n")

    except FileNotFoundError:
        print("No expenses found!\n")


# 4. Menu / Main function
def main():
    initialize_file()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Thank You.....Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


# Run Program
main()
