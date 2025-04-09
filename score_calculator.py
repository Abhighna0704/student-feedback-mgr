# Compute average score
def compute_average():
    with open("feedback_data.txt", "r") as f:
        scores = [float(line.strip().split(",")[1]) for line in f.readlines()]
    return sum(scores) / len(scores) if scores else 0.0
