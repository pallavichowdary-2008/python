
# Student Feedback Sentiment Scoring

n = int(input("Enter the number of feedback sentences: "))

positive_words = ["good", "excellent", "helpful", "interesting", "great"]
negative_words = ["bad", "poor", "boring", "difficult", "worst"]

feedback_list = []
scores = []

# Input and analyse feedback
for i in range(n):
    feedback = input("\nEnter feedback sentence: ").lower()

    positive_count = 0
    negative_count = 0

    # Count positive keywords
    for word in positive_words:
        if word in feedback:
            positive_count += 1

    # Count negative keywords
    for word in negative_words:
        if word in feedback:
            negative_count += 1

    # Calculate sentiment score
    score = positive_count - negative_count

    feedback_list.append(feedback)
    scores.append(score)

    print("Positive Indicators:", positive_count)
    print("Negative Indicators:", negative_count)
    print("Sentiment Score:", score)

    # Classify feedback
    if score >= 2:
        print("Sentiment: Very Positive")
    elif score == 1:
        print("Sentiment: Positive")
    elif score == 0:
        print("Sentiment: Neutral")
    elif score == -1:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Very Negative")

# Display summary
if n > 0:
    print("\n--- Feedback Summary ---")

    total_score = 0
    positive_feedback = 0
    negative_feedback = 0
    neutral_feedback = 0

    for i in range(n):
        total_score += scores[i]

        if scores[i] > 0:
            positive_feedback += 1
        elif scores[i] < 0:
            negative_feedback += 1
        else:
            neutral_feedback += 1

    print("Total Feedback:", n)
    print("Positive Feedback:", positive_feedback)
    print("Negative Feedback:", negative_feedback)
    print("Neutral Feedback:", neutral_feedback)
    print("Total Sentiment Score:", total_score)

else:
    print("No feedback available.")