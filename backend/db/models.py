import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
	__tablename__ = "users"

	id = Column(String, primary_key=True)
	firstName = Column(String)
	lastName = Column(String)
	email = Column(String, unique=True)
	password = Column(String)