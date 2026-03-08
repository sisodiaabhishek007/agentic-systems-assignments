from sqlalchemy import Table, update
from db_connection import engine, metadata

students = Table("students", metadata, autoload_with=engine)

conn = engine.connect()

query = update(students).where(students.c.name == "Rahul").values(city="Bangalore")

conn.execute(query)
conn.commit()

print("City updated for Rahul")
