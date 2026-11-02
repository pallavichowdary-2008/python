
# Tuple-Based Employee Shift Conflict Detection

n = int(input("Enter the number of employee shifts: "))

shifts = []
conflicts = []

# Input employee shift details
for i in range(n):
    print("\nShift", i + 1)

    employee = input("Enter employee name: ")
    start = int(input("Enter shift start time (0-23): "))
    end = int(input("Enter shift end time (1-24): "))

    # Validate shift timings
    if start < 0 or start > 23 or end < 1 or end > 24 or start >= end:
        print("Invalid shift timing!")
        break

    # Store shift as a tuple
    shift = (employee, start, end)
    shifts.append(shift)

# Check for overlapping shifts
if len(shifts) == n:

    print("\n--- Employee Shift Schedule ---")

    for shift in shifts:
        employee, start, end = shift
        print(employee, ":", start, "to", end)

    print("\n--- Shift Conflict Report ---")

    for i in range(n):
        for j in range(i + 1, n):

            emp1, start1, end1 = shifts[i]
            emp2, start2, end2 = shifts[j]

            # Check overlapping time intervals
            if start1 < end2 and start2 < end1:

                if emp1 == emp2:
                    conflict = (emp1, start1, end1,
                                start2, end2)
                    conflicts.append(conflict)

                    print("Conflict detected for:", emp1)
                    print("Shift 1:", start1, "to", end1)
                    print("Shift 2:", start2, "to", end2)
                    print()

    # Display final result
    if len(conflicts) == 0:
        print("No employee shift conflicts detected.")
    else:
        print("Total Conflicts Detected:", len(conflicts))

        print("\nEmployees with Conflicting Schedules:")

        for i in range(len(conflicts)):
            emp, s1, e1, s2, e2 = conflicts[i]

            already_printed = False

            for j in range(i):
                if conflicts[j][0] == emp:
                    already_printed = True

            if not already_printed:
                print(emp)

else:
    print("Schedule cannot be generated due to invalid input.")
