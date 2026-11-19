"""Builds school.db by running the SQL in school.sql.

Run it any time to reset the data:  python src/setup_db.py
(You don't need to understand this file - open school.sql instead!)

You do need to understand this file if you want to use the database in your own code.
"""
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent # the folder this file is in
DB_PATH = HERE.parent / "school.db" # the database file is in the parent folder

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.executescript((HERE / "school.sql").read_text())
    conn.close()
    print("Database reset: school.db")
