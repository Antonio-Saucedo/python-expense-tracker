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
        print("No expense.txt file was found.\nContinuing with empty expense list.")

def display_menu():
    print("\n====== Expense Tracker Menu ======")
    print("1. Add new expenses")
    print("2. View all expenses")
    print("3. View expense summary")
    print("4. Update expense")
    print("5. Delete expense")
    print("6. Save and exit")

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

        print(f"{category} expense was added for {description} with the amount of ${amount}")
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

def update_expense():
    if not expenses:
        print("No expenses have been added.")
        return

    print("\n====== Available Expenses ======")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")

    try:
        option = int(input(f"Which expense to update (1 - {len(expenses)}): "))

        if option <= len(expenses):
            try:
                print("\n====== Update Options ======")
                print("1. Expense amount")
                print("2. Expense category")
                print("3. Expense description")
                print("4. All of the above")
                expenseChangeOption = input("Choose an option (1-4): ")

                if expenseChangeOption in ("1", "4"):
                    amount = float(input('\nNew expense amount: $'))
                if expenseChangeOption in ("2", "4"):
                    category = input("New expense category: ")
                if expenseChangeOption in ("3", "4"):
                    description = input("New expense description: ")
                else:
                    print("Option not available.")

                if expenseChangeOption in ("1", "4"):
                    expenses[option - 1]['amount'] = amount
                if expenseChangeOption in ("2", "4"):
                    expenses[option - 1]['category'] = category
                if expenseChangeOption in ("3", "4"):
                    expenses[option - 1]['description'] = description
                if expenseChangeOption in ("1", "2", "3", "4") :
                    print(f"{expenses[option - 1]['category']} expense was updated for {expenses[option - 1]['description']} with the amount of ${expenses[option - 1]['amount']:.2f}")
            except ValueError:
                print("Please enter a numerical amount.")
        else:
            print("Option not available.")
    except ValueError:
        print("Please enter a whole numerical option.")

def delete_expense():
    if not expenses:
        print("No expenses have been added.")
        return

    print("\n====== Available Expenses ======")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")

    try:
        option = int(input(f"Which expense to delete (1 - {len(expenses)}): "))

        if option <= len(expenses):
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
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        update_expense()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        save_expenses()
        print("\nGoodbye, see you next time!")
        break
    else:
        print("\nPlease enter a valid option.")