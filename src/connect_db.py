from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

engine = create_engine("postgresql+psycopg2://postgres:qwerty@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()