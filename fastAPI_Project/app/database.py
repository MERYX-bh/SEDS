from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/database.db"
#Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)