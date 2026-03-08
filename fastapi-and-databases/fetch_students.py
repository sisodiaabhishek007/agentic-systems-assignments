from sqlalchemy import Table, select
from db_connection import engine, metadata

students = Table("students", metadata, autoload_with=engine)

conn = engine.connect()

query = select(students)

result = conn.execute(query)

for row in result:
    print(row)
