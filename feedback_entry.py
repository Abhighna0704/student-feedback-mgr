# Collect student feedback
def collect_feedback():
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))
    with open("feedback_data.txt", "a") as f:
        f.write(f"{name},{score}\n")
