
# Nested Loop Examination Seating Generator

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

capacity = rows * cols

print("Classroom Capacity:", capacity)

reserved_count = int(input("Enter the number of reserved seats: "))

reserved = []

# Input reserved seat positions
for i in range(reserved_count):
    print("Reserved Seat", i + 1)
    r = int(input("Enter row number: "))
    c = int(input("Enter column number: "))

    if r < 1 or r > rows or c < 1 or c > cols:
        print("Invalid seat position!")
        break

    reserved.append((r, c))

# Generate seating arrangement
if len(reserved) == reserved_count:

    print("\n--- Examination Seating Arrangement ---")

    student_number = 1
    occupied_count = 0

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):

            # Check whether the seat is reserved
            if (r, c) in reserved:
                print("RES", end="\t")

            # Alternate seating restriction:
            # Leave seats with even row + column sum empty
            elif (r + c) % 2 == 0:
                print("---", end="\t")

            else:
                print("S" + str(student_number), end="\t")
                student_number += 1
                occupied_count += 1

        print()

    print("\nTotal Classroom Capacity:", capacity)
    print("Reserved Seats:", reserved_count)
    print("Students Seated:", occupied_count)
    print("Unoccupied Seats:",
          capacity - reserved_count - occupied_count)

else:
    print("Seating arrangement cannot be generated.")
