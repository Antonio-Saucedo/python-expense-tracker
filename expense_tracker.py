import re

expenses = []

def get_expenses():
    pattern = re.compile(r'^\d+\.\s*(.+?):\s*\$(\d+(?:\.\d{2})?)\s*-\s*(.+)$')
    try:
        with open('./expense.txt', 'r') as file:
            for line in file:
                line = line.strip() # Remove leading/trailing whitespace
                if not line:
                    continue  # skip empty lines

                # Expected format: "{row_number}. {category}: ${amount} - {description}"
                match = pattern.match(line)
                if match:
                    category = match.group(1).strip()
                    amount = float(match.group(2))
                    description = match.group(3).strip()

                    expenses.append({
                        'amount': amount,
                        'category': category,
                        'description': description
                    })
                else:
                    # print(f"line: {line}")
                    pass
    except FileNotFoundError:
        print("No file was found.\nContinuing with empty expense list.")

def display_menu():
    print("\n====== Expense Tracker Menu ======")
    print("1. Add new expenses")
    print("2. View all expenses")
    print("3. View expense summary")
    print("4. Delete expense")
    print("5. Save and exit")

def add_expense():
    try:
        amount = float(input('\nExpense amount: $'))
        category = input("Expense category: ")
        description = input("Expense description: ")

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })

        print(f"{category} expense was added for {description} of the amount of ${amount}")
    except ValueError:
        print("Please enter a numerical amount.")

def view_expenses():
    if not expenses:
        print("No expenses have been added.")
        return

    print("\n====== All Expenses ======")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")

def view_summary():
    if not expenses:
        print("No expenses have been added.")
        return

    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']
    print("\n====== Expense Summary ======")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

def delete_expense():
    if not expenses:
        print("No expenses have been added.")
        return

    print("\n====== Available Expenses ======")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")

    try:
        option = int(input(f"Which expense to delete (1 - {len(expenses)}): "))

        if option < len(expenses):
            expenses.pop(option - 1)
        else:
            print("Option not available.")
    except ValueError:
        print("Please enter a whole numerical option.")

def save_expenses():
    with open('./expense.txt', "w") as file:
        for i, expense in enumerate(expenses, 1):
            file.write(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}\n")
    print("Expenses saved sucessfully.")

get_expenses()

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        save_expenses()
        print("\nGoodbye, see you next time!")
        break
    else:
        print("\nPlease enter a valid option.")