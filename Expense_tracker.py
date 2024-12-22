transactions = []

while True:
    print("\n1. Add Income\n2. Add Expense\n3. View Transactions\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        transactions.append(("Income", amount))
    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        transactions.append(("Expense", amount))
    elif choice == "3":
        for t_type, amount in transactions:
            print(f"{t_type}: ${amount:.2f}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
