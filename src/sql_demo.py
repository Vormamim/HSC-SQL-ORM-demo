"""CONCEPT 1 (part A): Plain SQL - retrieve and add data.

Run:  python src/sql_demo.py
Edit the SQL strings below and re-run to experiment!
"""
import sqlite3
from setup_db import DB_PATH

conn = sqlite3.connect(DB_PATH) # connect to the database file (creates it if it doesn't exist)
cur = conn.cursor() # create a "cursor" object to run SQL commands and fetch results

# ---------------------------------------------------------------------------
# 1. SELECT - retrieve data
# ---------------------------------------------------------------------------
# SELECT name, year   -> which COLUMNS we want back
# FROM student        -> which TABLE to read
# WHERE year = 12     -> only ROWS that match this condition
# ORDER BY name       -> sort the results A-Z
sql = "SELECT name, year FROM student WHERE year = 12 ORDER BY name"
print("SQL:", sql)
for row in cur.execute(sql):
    print("  ", row)

# ---------------------------------------------------------------------------
# 2. SELECT with a parameter - safe way to use a variable
# ---------------------------------------------------------------------------
# The ? is a placeholder. NEVER build SQL by gluing strings together with
# user input (f"... {name} ...") - that allows SQL injection attacks.
wanted_year = 11
sql = "SELECT name, email FROM student WHERE year = ?"
print("\nSQL:", sql, "| ? =", wanted_year)
for row in cur.execute(sql, (wanted_year,)):
    print("  ", row)

# ---------------------------------------------------------------------------
# 3. JOIN - combine data from several tables
# ---------------------------------------------------------------------------
# Each enrolment row links a student to a course. JOIN follows those links.
sql = """
SELECT student.name, course.title
FROM enrolment
JOIN student ON student.id = enrolment.student_id
JOIN course  ON course.id  = enrolment.course_id
WHERE course.title = 'Software Engineering'
"""
print("\nSQL:", " ".join(sql.split()))
for row in cur.execute(sql):
    print("  ", row)

# ---------------------------------------------------------------------------
# 4. INSERT - add data
# ---------------------------------------------------------------------------
# INSERT INTO student (...)  -> table and the columns we are filling in
# VALUES (?, ?, ?)           -> the values, in the same order
# 'id' is left out: the database assigns it automatically.
sql = "INSERT INTO student (name, year, email) VALUES (?, ?, ?)"
cur.execute(sql, ("Ethan Lee", 12, "ethan@example.com"))
conn.commit()  # without commit(), the change is NOT saved!
print("\nInserted Ethan Lee, new id =", cur.lastrowid)

# Check it worked: COUNT(*) counts rows
print("Total students now:", cur.execute("SELECT COUNT(*) FROM student").fetchone()[0])

conn.close()
print("\n(Run `python src/setup_db.py` to reset the data.)")
