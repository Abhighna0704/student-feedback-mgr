import score_calculator

def test_compute_average(tmp_path):
    file = tmp_path / "feedback_data.txt"
    file.write_text("Alice,90\nBob,80\n")
    with open("feedback_data.txt", "w") as f:
        f.write("Alice,90\nBob,80\n")
    assert score_calculator.compute_average() == 85.0
