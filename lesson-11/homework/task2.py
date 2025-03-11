import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

cursor.execute("DELETE FROM Books")  

cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

conn.commit()

cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

conn.commit()

cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
print("Dystopian Books:")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

conn.commit()

cursor.execute("SELECT * FROM Books")
print("\nRemaining Books in Library:")
for row in cursor.fetchall():
    print(row)

conn.close()
