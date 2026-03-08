from sqlalchemy import create_engine, MetaData

# SQLite database (auto created)
DATABASE_URL = "sqlite:///student_db.db"

engine = create_engine(DATABASE_URL)

metadata = MetaData()
