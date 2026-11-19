# SQL vs ORM (reading)

**SQL** is a language you send straight to the database.
**ORM** (Object-Relational Mapping) is a library that lets you use Python classes and objects instead, and writes the SQL for you.

## SQL

| Advantages | Disadvantages |
|---|---|
| **Full control and clarity** – you see exactly what runs; complex queries are often shorter and easier to optimise. | **Mixes two languages** – SQL sits in Python strings, so typos only show up when you run it. |
| **Universal skill** – works with any relational database and any language. | **Repetitive** – every query is written by hand, and joining strings instead of using `?` risks SQL injection. |

## ORM

| Advantages | Disadvantages |
|---|---|
| **Work in Python** – rows are objects (`student.name`), so there is less code and parameters are escaped automatically. | **Hides the SQL** – it can generate slow queries and is harder to debug. |
| **Portable** – switching database needs little code change. | **Extra learning** – you must learn the library and still understand SQL. |

## Your turn

Complete: "I would choose ______ when ______ because ______."
