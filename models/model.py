from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
