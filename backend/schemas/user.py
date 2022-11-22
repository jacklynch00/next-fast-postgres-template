from uuid import UUID
from pydantic import BaseModel

class UserBase(BaseModel):
	firstName: str
	lastName: str
	email: str

class NewUser(UserBase):
	password: str

class User(UserBase):
	id: UUID
	password: str

	class Config:
		orm_mode = True