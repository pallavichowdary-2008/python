
# Multi-Currency Travel Budget Analysis

n = int(input("Enter the number of expense categories: "))

categories = []
converted_expenses = []

budget = float(input("Enter total travel budget in INR: "))
fee_percent = float(input("Enter currency conversion fee percentage: "))

# Validate budget and conversion fee
if n <= 0 or budget < 0 or fee_percent < 0:
    print("Invalid input!")
else:
    # Input expense details
    for i in range(n):
        print("\nExpense Category", i + 1)

        category = input("Enter category name: ")
        amount = float(input("Enter expense amount in foreign currency: "))
        exchange_rate = float(input("Enter exchange rate (INR per unit): "))

        if amount < 0 or exchange_rate <= 0:
            print("Invalid amount or exchange rate!")
            break

        # Convert expense into INR
        converted_amount = amount * exchange_rate

        # Calculate conversion fee
        conversion_fee = converted_amount * fee_percent / 100

        # Total expense including conversion fee
        total_expense = converted_amount + conversion_fee

        categories.append(category)
        converted_expenses.append(total_expense)

        print("Expense in INR: Rs.", round(converted_amount, 2))
        print("Conversion Fee: Rs.", round(conversion_fee, 2))
        print("Total Expense: Rs.", round(total_expense, 2))

    # Generate report if all entries are valid
    if len(categories) == n:
        total_spending = 0
        largest_expense = 0
        largest_category = categories[0]

        print("\n--- Travel Expense Report ---")

        for i in range(n):
            print(categories[i], ": Rs.",
                  round(converted_expenses[i], 2))

            total_spending += converted_expenses[i]

            # Identify the largest expense category
            if converted_expenses[i] > largest_expense:
                largest_expense = converted_expenses[i]
                largest_category = categories[i]

        print("\nTotal Travel Spending: Rs.",
              round(total_spending, 2))
        print("Travel Budget: Rs.", round(budget, 2))
        print("Largest Expense Category:", largest_category)
        print("Largest Expense Amount: Rs.",
              round(largest_expense, 2))

        # Compare spending against budget
        if total_spending > budget:
            excess = total_spending - budget
            print("Budget Status: OVER BUDGET")
            print("Amount Exceeded: Rs.", round(excess, 2))

        elif total_spending < budget:
            remaining = budget - total_spending
            print("Budget Status: WITHIN BUDGET")
            print("Remaining Budget: Rs.", round(remaining, 2))

        else:
            print("Budget Status: EXACTLY ON BUDGET")

    else:
        print("Report cannot be generated because the input is invalid.")
