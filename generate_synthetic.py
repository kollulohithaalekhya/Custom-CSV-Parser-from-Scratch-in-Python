"""generate_synthetic.py

Generate a synthetic CSV file with edge cases for benchmarking and testing.
"""
import random
import csv

SAMPLE_TEXTS = [
    "simple",
    "contains,comma",
    'contains"quote"',
    "multiline\nline2",
    "normal",
]


def generate(path: str, rows: int = 10000, cols: int = 5) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = []
            for c in range(cols):
                choice = random.choice(SAMPLE_TEXTS)
                row.append(f"{choice}_{i}_{c}")
            writer.writerow(row)


if __name__ == "__main__":
    generate("synthetic.csv", rows=10000, cols=5)
