# Database Connection and Session Management

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
database_url = 'sqlite:///./test.db'  # Replace with your actual database URL

# Create a database engine
engine = create_engine(database_url, connect_args={"check_same_thread": False})

# Create a configured "Session" class
session = sessionmaker(bind=engine)

# Create a session instance
session_instance = session()

# Function to close the session

def close_session():
    session_instance.close()