from sqlalchemy import Table, Column, Integer, String
from db_connection import engine, metadata

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
    Column("city", String, nullable=True)
)

metadata.create_all(engine)

print("Students table created")
