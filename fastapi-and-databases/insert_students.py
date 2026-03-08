from sqlalchemy import Table, insert
from db_connection import engine, metadata

students = Table("students", metadata, autoload_with=engine)

conn = engine.connect()

query = insert(students).values([
    {"name": "Rahul", "age": 22, "city": "Delhi"},
    {"name": "Aman", "age": 19, "city": "Mumbai"},
    {"name": "Priya", "age": 25, "city": "Pune"}
])

conn.execute(query)
conn.commit()

print("Students inserted")
