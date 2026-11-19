-- school.sql: builds the whole database. Read it top to bottom!
-- Running setup_db.py runs every statement in this file.

-- Start fresh: delete the tables if they already exist
DROP TABLE IF EXISTS enrolment;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;

-- CREATE TABLE makes a table. Each line inside is a column and its type.
CREATE TABLE student (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,  -- unique number, set automatically
    name  TEXT NOT NULL,                      -- NOT NULL = must have a value
    year  INTEGER NOT NULL,
    email TEXT                                -- can be empty (NULL)
);

CREATE TABLE course (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

-- Links students to courses: one row = one student in one course
CREATE TABLE enrolment (
    student_id INTEGER NOT NULL REFERENCES student(id),
    course_id  INTEGER NOT NULL REFERENCES course(id)
);

-- INSERT INTO adds a row. Values go in the same order as the column list.
INSERT INTO student (name, year, email) VALUES ('Ava Nguyen',   11, 'ava@example.com');
INSERT INTO student (name, year, email) VALUES ('Liam Smith',   12, 'liam@example.com');
INSERT INTO student (name, year, email) VALUES ('Mia Patel',    11, 'mia@example.com');
INSERT INTO student (name, year, email) VALUES ('Noah Brown',   12, NULL);
INSERT INTO student (name, year, email) VALUES ('Zoe Williams', 11, 'zoe@example.com');

INSERT INTO course (title) VALUES ('Software Engineering');
INSERT INTO course (title) VALUES ('Mathematics');
INSERT INTO course (title) VALUES ('Physics');

-- (student_id, course_id): e.g. student 1 (Ava) is in course 1 (Software Engineering)
INSERT INTO enrolment (student_id, course_id) VALUES (1, 1);
INSERT INTO enrolment (student_id, course_id) VALUES (1, 2);
INSERT INTO enrolment (student_id, course_id) VALUES (2, 1);
INSERT INTO enrolment (student_id, course_id) VALUES (3, 1);
INSERT INTO enrolment (student_id, course_id) VALUES (3, 3);
INSERT INTO enrolment (student_id, course_id) VALUES (4, 2);
INSERT INTO enrolment (student_id, course_id) VALUES (5, 1);
INSERT INTO enrolment (student_id, course_id) VALUES (5, 2);
