
# Smart Canteen Order and Stock Management

items = ["Idli", "Dosa", "Meals", "Juice", "Tea"]
prices = [30, 50, 80, 40, 15]
stock = [50, 40, 30, 25, 60]

total_sales = 0
total_orders = 0

print("--- Canteen Menu ---")

for i in range(len(items)):
    print(i + 1, items[i], "- Rs.", prices[i],
          "| Available:", stock[i])

orders = int(input("\nEnter the number of customer orders: "))

# Process customer orders
if orders < 0:
    print("Invalid number of orders!")

else:
    for i in range(orders):
        print("\nCustomer Order", i + 1)

        item_number = int(input("Enter item number (1-5): "))
        quantity = int(input("Enter quantity: "))

        # Validate item number and quantity
        if item_number < 1 or item_number > len(items):
            print("Invalid item number!")

        elif quantity <= 0:
            print("Invalid quantity!")

        else:
            index = item_number - 1

            # Check stock availability
            if quantity > stock[index]:
                print("Order rejected!")
                print("Only", stock[index], items[index],
                      "available.")

            else:
                # Calculate bill
                bill = prices[index] * quantity

                # Update inventory
                stock[index] = stock[index] - quantity

                # Update daily sales
                total_sales = total_sales + bill
                total_orders = total_orders + 1

                print("Item:", items[index])
                print("Quantity:", quantity)
                print("Total Bill: Rs.", bill)
                print("Order successful!")

    # Daily sales summary
    print("\n--- Daily Sales Summary ---")
    print("Successful Orders:", total_orders)
    print("Total Sales: Rs.", total_sales)

    # Remaining stock report
    print("\n--- Remaining Stock ---")

    for i in range(len(items)):
        print(items[i], ":", stock[i], "units")

    print("\nCanteen report generated successfully.")
