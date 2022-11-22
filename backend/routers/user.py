from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import UserDB, sqlalchemy_db
from db.models import User as DBUser
from schemas.user import UserBase, User, NewUser

router = APIRouter(prefix="/user")

@router.get('/')
async def get_all_users(db: Session = Depends(sqlalchemy_db)):
	user =  UserDB.get_all_users(db)
	return user

@router.get('/{user_id}', response_model=User)
async def get_user(user_id: str, db: Session = Depends(sqlalchemy_db)):
	user =  UserDB.get_user_by_id(db, user_id)
	if user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return user

@router.post('/', response_model=User)
async def create_user(user_info: NewUser, db: Session = Depends(sqlalchemy_db)):
	user =  UserDB.get_user(db, user_info.email)
	if user:
		raise HTTPException(status_code=400, detail="User with that email already exists")
	return UserDB.create_user(db, new_user=user_info)

@router.delete('/{user_id}')
async def delete_user(user_id: str, db: Session = Depends(sqlalchemy_db)):
	user_db = UserDB.get_user_by_id(db, user_id)
	if user_db:
		try:
			UserDB.delete_user(db, user_id)
			return user_db
		except:
			raise HTTPException(status_code=400, detail="An error occurred while deleting the user")
	else:
		raise HTTPException(status_code=404, detail="User associated with this ID not found")