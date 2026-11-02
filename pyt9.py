
# Hospital Resource Allocation and Capacity Monitoring

wards = ["Emergency", "General", "ICU", "Maternity"]

# Nested lists: [beds occupied, total beds, available staff, required staff,
#                available equipment, required equipment]
resources = [
    [18, 20, 3, 5, 4, 5],
    [35, 40, 8, 7, 10, 8],
    [9, 10, 4, 6, 3, 5],
    [12, 15, 4, 4, 6, 5]
]

priorities = []

print("--- Hospital Resource Status ---")

# Analyse resources in each ward
for i in range(len(wards)):
    occupied = resources[i][0]
    total_beds = resources[i][1]
    available_staff = resources[i][2]
    required_staff = resources[i][3]
    available_equipment = resources[i][4]
    required_equipment = resources[i][5]

    available_beds = total_beds - occupied
    occupancy = (occupied / total_beds) * 100

    print("\nWard:", wards[i])
    print("Total Beds:", total_beds)
    print("Occupied Beds:", occupied)
    print("Available Beds:", available_beds)
    print("Bed Occupancy:", round(occupancy, 2), "%")
    print("Available Staff:", available_staff)
    print("Required Staff:", required_staff)
    print("Available Equipment:", available_equipment)
    print("Required Equipment:", required_equipment)

    shortage = 0

    # Check bed shortage
    if available_beds <= 2:
        print("Warning: Bed capacity is critical!")
        shortage += 1

    # Check staff shortage
    if available_staff < required_staff:
        print("Warning: Staff shortage detected!")
        shortage += 1

    # Check equipment shortage
    if available_equipment < required_equipment:
        print("Warning: Equipment shortage detected!")
        shortage += 1

    priorities.append(shortage)

# Prioritize wards based on number of shortages
print("\n--- Resource Allocation Priority ---")

for i in range(len(wards)):
    if priorities[i] >= 2:
        print(wards[i], ": HIGH PRIORITY")
    elif priorities[i] == 1:
        print(wards[i], ": MEDIUM PRIORITY")
    else:
        print(wards[i], ": LOW PRIORITY")

# Identify the ward with the most shortages
highest = max(priorities)

print("\n--- Final Summary ---")

if highest == 0:
    print("No resource shortages detected.")
else:
    print("Ward(s) requiring the most urgent attention:")

    for i in range(len(wards)):
        if priorities[i] == highest:
            print(wards[i], "-", highest, "resource shortage(s)")
