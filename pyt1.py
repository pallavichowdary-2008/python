
# Examination Result and Grace-Mark Validation

n = int(input("Enter the number of subjects: "))
max_marks = int(input("Enter maximum marks per subject: "))
pass_marks = int(input("Enter minimum passing marks: "))
grace_limit = int(input("Enter maximum grace marks allowed: "))

marks = []
final_marks = []
total = 0
grace_used = 0

# Input marks for each subject
for i in range(n):
    m = int(input("Enter marks for subject " + str(i + 1) + ": "))

    if m < 0 or m > max_marks:
        print("Invalid marks! Enter marks between 0 and", max_marks)
        break

    marks.append(m)

# Process results only if all marks are valid
if len(marks) == n:

    for i in range(n):
        m = marks[i]

        if m < pass_marks:
            required = pass_marks - m

            if required <= grace_limit - grace_used and m + required <= max_marks:
                m = m + required
                grace_used = grace_used + required

        final_marks.append(m)
        total = total + m

    # Display subject-wise results
    print("\n--- Examination Result ---")

    for i in range(n):
        print("Subject", i + 1)
        print("Original Marks:", marks[i])
        print("Final Marks:", final_marks[i])

        if final_marks[i] >= pass_marks:
            print("Status: PASS")
        else:
            print("Status: FAIL")

    # Calculate percentage
    percentage = (total / (n * max_marks)) * 100

    print("\nTotal Marks:", total)
    print("Maximum Total Marks:", n * max_marks)
    print("Percentage:", round(percentage, 2), "%")
    print("Grace Marks Used:", grace_used)

    # Final classification
    failed = 0

    for i in range(n):
        if final_marks[i] < pass_marks:
            failed = failed + 1

    if failed > 0:
        print("Final Result: FAIL")
    elif percentage >= 75:
        print("Final Classification: DISTINCTION")
    elif percentage >= 60:
        print("Final Classification: FIRST CLASS")
    elif percentage >= 50:
        print("Final Classification: SECOND CLASS")
    else:
        print("Final Classification: PASS")

else:
    print("Result cannot be generated because the marks entered are invalid.")
