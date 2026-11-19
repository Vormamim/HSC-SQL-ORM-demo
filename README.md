# Learn SQL — Hands-on Demo

Learn to **write a simple SQL statement to retrieve or add data, and explain what it does.**

You only need Python (SQLite is built in). Nothing to install.

## Setup

```bash
git clone <this-repo-url>
cd <repo-folder>
python src/setup_db.py        # creates school.db with sample data
```

## The database

```
student   (id, name, year, email)
course    (id, title)
enrolment (student_id, course_id)   <- links students to courses
```

## Activities

| Step | Do this | What you learn |
|------|---------|----------------|
| 1 | Read [src/school.sql](src/school.sql) | How tables are created and filled (`CREATE TABLE`, `INSERT INTO`) |
| 2 | Run `python src/sql_demo.py` | `SELECT`, `WHERE`, `ORDER BY`, `JOIN`, `INSERT` — each one explained in comments |
| 3 | Edit the SQL in `sql_demo.py`, run it again | Experiment! |
| 4 | Work through [EXERCISES.md](EXERCISES.md) | Write your own SQL |
| 5 | Read [COMPARISON.md](COMPARISON.md) | SQL vs ORM: advantages and disadvantages |

Reset the data any time with `python src/setup_db.py`.

**Tip:** open `school.db` in [DB Browser for SQLite](https://sqlitebrowser.org/) or the "SQLite Viewer" VS Code extension to see the tables.
