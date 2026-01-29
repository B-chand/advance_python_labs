"""
Lab Report: Database Management in Python
Topic: SQLite, SQLAlchemy, and NoSQL Integration

-------------------------------------------------
OBJECTIVES:
- Implement a local relational database using SQLite
- Abstract database interactions using SQLAlchemy ORM
- Understand document-oriented data storage using MongoDB (NoSQL)

-------------------------------------------------
THEORY:
Databases are essential for storing and managing application data.
Python supports both relational (SQL) and non-relational (NoSQL) databases.

SQLite:
- Lightweight, serverless relational database
- Stores data in a single file
- Uses SQL queries
- Suitable for small applications and learning

SQLAlchemy ORM:
- Object Relational Mapper for Python
- Converts database tables into Python classes
- Avoids writing raw SQL
- Improves maintainability and security

MongoDB (NoSQL):
- Document-oriented database
- Stores data as JSON-like documents
- Schema-less and flexible
- Suitable for unstructured and scalable applications
-------------------------------------------------
"""

# =================================================
# PART 1: SQLITE IMPLEMENTATION
# =================================================

import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("students_sqlite.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade REAL
)
""")

# Insert records
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 85.5))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Bob", 90.0))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Charlie", 88.5))

conn.commit()

# Retrieve and display records
print("=== SQLite Output ===")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()

# =================================================
# PART 2: SQLALCHEMY ORM IMPLEMENTATION
# =================================================

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for ORM models
Base = declarative_base()

# ORM model representing a table
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(Float)

# Create database and tables
engine = create_engine("sqlite:///students_sqlalchemy.db")
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert records using Python objects
students = [
    Student(name="Diana", grade=92.0),
    Student(name="Emma", grade=87.5),
    Student(name="Frank", grade=95.0)
]

session.add_all(students)
session.commit()

# Query and display records
print("\n=== SQLAlchemy Output ===")
for student in session.query(Student).all():
    print(student.name, student.grade)

session.close()

# =================================================
# PART 3: MONGODB (NoSQL) IMPLEMENTATION
# =================================================

from pymongo import MongoClient

# NOTE:
# Ensure MongoDB is running locally OR replace URI with MongoDB Atlas URI
client = MongoClient("mongodb://localhost:27017/")

# Create database and collection
db = client["college_db"]
collection = db["students"]

# Insert document (No fixed schema)
student_document = {
    "name": "Grace",
    "grade": 91,
    "skills": ["Python", "Databases"]
}

collection.insert_one(student_document)

# Retrieve and display documents
print("\n=== MongoDB Output ===")
for doc in collection.find():
    print(doc)

client.close()

# =================================================
# CONCLUSION (COMMENT)
# =================================================
"""
CONCLUSION:
This program demonstrates three database approaches in Python.

- SQLite uses raw SQL and is suitable for simple, local databases.
- SQLAlchemy ORM provides an object-oriented way to interact with relational databases.
- MongoDB stores flexible, document-based data without a fixed schema.

Each database approach serves different application needs.
Choosing the correct database depends on scalability, structure, and complexity.
"""

# =================================================
# END OF LAB
# =================================================