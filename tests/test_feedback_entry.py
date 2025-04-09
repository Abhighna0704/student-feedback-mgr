import os
import feedback_entry

def test_collect_feedback(monkeypatch):
    # Simulate user input for name and score
    monkeypatch.setattr('builtins.input', lambda prompt: 'Alice' if 'name' in prompt else '95')

    # Remove file if exists
    if os.path.exists("feedback_data.txt"):
        os.remove("feedback_data.txt")

    feedback_entry.collect_feedback()

    with open("feedback_data.txt", "r") as f:
        data = f.read().strip()

    assert data == "Alice,95"
