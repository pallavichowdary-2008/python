
# Progressive Electricity Billing

months = int(input("Enter the number of months: "))

bills = []
units_list = []

# Input billing details
for i in range(months):
    print("\nMonth", i + 1)

    units = int(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a non-negative value.")
        break

    # Calculate charges using progressive slabs
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)
    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    # Fixed charge
    fixed_charge = 50

    # Surcharge: 5% if consumption exceeds 300 units
    if units > 300:
        surcharge = energy_charge * 0.05
    else:
        surcharge = 0

    # Rebate: 10% on energy charge if consumption is 100 units or less
    if units <= 100:
        rebate = energy_charge * 0.10
    else:
        rebate = 0

    # Final bill
    bill = energy_charge + fixed_charge + surcharge - rebate

    bills.append(bill)
    units_list.append(units)

# Display bills if all inputs are valid
if len(bills) == months:

    print("\n--- Monthly Electricity Bills ---")

    for i in range(months):
        print("Month", i + 1)
        print("Units Consumed:", units_list[i])
        print("Electricity Bill: Rs.", round(bills[i], 2))

    # Calculate total and average bill
    total_bill = 0

    for i in range(months):
        total_bill = total_bill + bills[i]

    average_bill = total_bill / months

    print("\nTotal Bill: Rs.", round(total_bill, 2))
    print("Average Monthly Bill: Rs.", round(average_bill, 2))

    # Identify unusual increases
    print("\n--- Bill Increase Analysis ---")

    for i in range(1, months):
        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            increase_percent = (increase / bills[i - 1]) * 100
        else:
            increase_percent = 0

        print("Month", i + 1, "Bill Change: Rs.", round(increase, 2))

        if increase_percent > 25:
            print("Warning: Unusual bill increase detected!")
        else:
            print("No unusual increase detected.")

else:
    print("Billing report cannot be generated because the input is invalid.")