import csv
from collections import defaultdict

file_path = "d:/my_first_code/lesson-9/grades.csv"  # Full path

# Step 1: Read data from grades.csv
grades = defaultdict(list)

try:
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row["Subject"]
            grade = int(row["Grade"])
            grades[subject].append(grade)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path.")

# Step 2: Calculate average grades
if grades:
    average_grades = {subject: sum(scores) / len(scores) for subject, scores in grades.items()}

    # Step 3: Write to average_grades.csv
    output_path = "d:/my_first_code/lesson-9/average_grades.csv"
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in average_grades.items():
            writer.writerow([subject, round(avg, 2)])

    print(f"Average grades calculated and saved in '{output_path}'.")
