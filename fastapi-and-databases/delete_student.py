from sqlalchemy import Table, delete
from db_connection import engine, metadata

students = Table("students", metadata, autoload_with=engine)

conn = engine.connect()

query = delete(students).where(students.c.age < 20)

conn.execute(query)
conn.commit()

print("Students with age < 20 deleted")
