import uuid
from sqlalchemy.orm import Session

from db.models import User
from schemas.user import NewUser

class UserCRUD():
	def create_user(self, db: Session, new_user: NewUser):
		fake_hashed_password = new_user.password + "notreallyhashed"
		db_user = User(id=str(uuid.uuid4()), firstName=new_user.firstName, lastName=new_user.lastName, email=new_user.email, password=fake_hashed_password)
		db.add(db_user)
		db.commit()
		db.refresh(db_user)
		return db_user

	def get_all_users(self, db: Session):
		return db.query(User).all()

	def get_user(self, db: Session, user_email: str):
		return db.query(User).filter(User.email == user_email).first()
	
	def get_user_by_id(self, db: Session, user_id: str) -> User | None:
		return db.query(User).filter(User.id == user_id).first()

	def delete_user(self, db: Session, user_id: int):
		db.query(User).filter(User.id == user_id).delete()
		db.commit()
		return user_id