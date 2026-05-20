from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql://pguser:userpass@localhost:5432/mydatabase"

engine = create_engine(
    DATABASE_URL    
)

if not database_exists(engine.url):
    create_database(engine.url)
    print("Database 'my_new_db' created successfully!")
else:
    print("Database already exists.")

