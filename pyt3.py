
# Manufacturing Cost and Profitability Analysis

products = int(input("Enter the number of products: "))

product_names = []
total_costs = []
profits = []

# Input production details
for i in range(products):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity produced: "))
    material_cost = float(input("Enter material cost per unit: "))
    labour_cost = float(input("Enter labour cost per unit: "))
    machine_cost = float(input("Enter machine cost per unit: "))
    wastage_percent = float(input("Enter wastage percentage: "))
    selling_price = float(input("Enter selling price per unit: "))
    profit_target = float(input("Enter target profit percentage: "))

    # Validate input
    if (quantity <= 0 or material_cost < 0 or labour_cost < 0
            or machine_cost < 0 or wastage_percent < 0
            or wastage_percent > 100 or selling_price < 0
            or profit_target < 0):
        print("Invalid input! Please enter valid values.")
        break

    # Calculate material cost including wastage
    effective_material_cost = material_cost * (1 + wastage_percent / 100)

    # Calculate total cost per unit
    cost_per_unit = effective_material_cost + labour_cost + machine_cost

    # Calculate total production cost
    total_cost = cost_per_unit * quantity

    # Calculate total revenue
    revenue = selling_price * quantity

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Store results
    product_names.append(name)
    total_costs.append(total_cost)
    profits.append(profit)

    # Display product details
    print("\n--- Product Analysis ---")
    print("Product Name:", name)
    print("Effective Material Cost per Unit: Rs.",
          round(effective_material_cost, 2))
    print("Total Cost per Unit: Rs.", round(cost_per_unit, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    # Check profit target
    if profit > 0 and profit_percentage >= profit_target:
        print("Status: Profit target achieved")
    elif profit > 0:
        print("Status: Profit earned, but target not achieved")
    else:
        print("Status: No profit or loss")

# Display summary if all products were processed
if len(product_names) == products:
    print("\n--- Overall Manufacturing Summary ---")

    total_production_cost = 0
    total_profit = 0

    for i in range(products):
        total_production_cost += total_costs[i]
        total_profit += profits[i]

    print("Total Production Cost: Rs.",
          round(total_production_cost, 2))
    print("Total Profit/Loss: Rs.", round(total_profit, 2))

    if total_profit > 0:
        print("Overall Result: Manufacturing is profitable")
    elif total_profit < 0:
        print("Overall Result: Manufacturing is running at a loss")
    else:
        print("Overall Result: Break-even")
else:
    print("Summary cannot be generated because the input is invalid.")
