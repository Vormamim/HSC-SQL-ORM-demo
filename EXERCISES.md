# Exercises

Write your SQL in `src/sql_demo.py` (or a new file), run it, and reset the data with `python src/setup_db.py`.
For each task, **explain in one sentence what each part of your SQL does.**

## Retrieve data

1. Get the names of all Year 11 students.
2. Get all students sorted by name, Z to A (hint: `DESC`).
3. Get every student with no email (hint: `WHERE email IS NULL`).
4. Count the students in Mathematics (hint: `JOIN` and `COUNT(*)`).

## Add data

5. Add a new student of your own with `INSERT INTO`, then `SELECT` them to prove it worked.
6. Enrol your student in a course by inserting a row into `enrolment`.

## Challenges

7. What happens if you forget `conn.commit()` after an INSERT? Try it.
8. Try `INSERT INTO student (year) VALUES (11)`. Why does it fail?
