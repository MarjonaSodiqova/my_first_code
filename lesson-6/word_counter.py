import string
from collections import Counter
import os

file_path = "sample.txt"
report_path = "word_count_report.txt"

if not os.path.exists(file_path):
    print("File 'sample.txt' not found.")
    text = input("Please enter a paragraph to create 'sample.txt': ")
    with open(file_path, 'w') as file:
        file.write(text)
    print("File 'sample.txt' created successfully.")

with open(file_path, 'r') as file:
    content = file.read().lower()

content = content.translate(str.maketrans('', '', string.punctuation))

words = content.split()

word_count = Counter(words)

total_words = sum(word_count.values())

top_5_words = word_count.most_common(5)

print(f"Total number of words: {total_words}")
print("Top 5 most common words:")
for word, count in top_5_words:
    print(f"{word}: {count}")

with open(report_path, 'w') as report_file:
    report_file.write(f"Total number of words: {total_words}\n")
    report_file.write("Top 5 most common words:\n")
    for word, count in top_5_words:
        report_file.write(f"{word}: {count}\n")

print(f"Report saved to '{report_path}'.")
