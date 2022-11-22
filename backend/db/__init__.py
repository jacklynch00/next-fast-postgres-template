from sqlalchemy.orm import Session

from config import config
from db.models import User
from db.crud import UserCRUD
from db.utils import session_factory, sqlalchemy_dependency_generator

sqlalchemy_db = sqlalchemy_dependency_generator(config)

UserDB = UserCRUD()

def db_conn() -> Session:
    session = session_factory(config)
    return session()
