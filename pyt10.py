
# Multi-Event Sports Scheduling and Scoring

teams = ["Team A", "Team B", "Team C", "Team D"]

# Team scores for three events
scores = [
    [10, 20, 15],
    [25, 10, 20],
    [15, 25, 10],
    [20, 15, 25]
]

# Event schedules stored as tuples:
# (event name, start time, end time, venue)

schedules = [
    ("Football", 9, 11, "Ground A"),
    ("Basketball", 10, 12, "Ground B"),
    ("Volleyball", 12, 14, "Ground A"),
    ("Cricket", 14, 16, "Ground C")
]

print("--- Sports Event Schedule ---")

for event in schedules:
    name, start, end, venue = event
    print(name, ":", start, "to", end, "| Venue:", venue)

# Check scheduling conflicts at the same venue
print("\n--- Scheduling Conflict Report ---")

conflicts = 0

for i in range(len(schedules)):
    for j in range(i + 1, len(schedules)):

        name1, start1, end1, venue1 = schedules[i]
        name2, start2, end2, venue2 = schedules[j]

        # Events conflict if they overlap at the same venue
        if venue1 == venue2 and start1 < end2 and start2 < end1:
            print("Conflict:", name1, "and", name2)
            print("Venue:", venue1)
            conflicts += 1

if conflicts == 0:
    print("No scheduling conflicts detected.")

# Calculate total points for each team
totals = []

print("\n--- Team Scores ---")

for i in range(len(teams)):
    total = 0

    for j in range(len(scores[i])):
        total += scores[i][j]

    totals.append(total)

    print(teams[i], "Scores:", scores[i],
          "| Total Points:", total)

# Generate final rankings
print("\n--- Final Team Rankings ---")

for position in range(len(teams)):
    highest_index = position

    for j in range(position + 1, len(teams)):
        if totals[j] > totals[highest_index]:
            highest_index = j

    # Swap totals
    temp = totals[position]
    totals[position] = totals[highest_index]
    totals[highest_index] = temp

    # Swap team names
    temp_team = teams[position]
    teams[position] = teams[highest_index]
    teams[highest_index] = temp_team

    # Swap score lists
    temp_score = scores[position]
    scores[position] = scores[highest_index]
    scores[highest_index] = temp_score

    print(position + 1, teams[position],
          "- Total Points:", totals[position])

print("\nSports event analysis completed.")
