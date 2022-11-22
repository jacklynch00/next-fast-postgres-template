from typing import Callable, Any, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config


def session_factory(config: Config) -> sessionmaker:
		engine = create_engine(config.postgres_url())
		return sessionmaker(bind=engine, autocommit=False, autoflush=False)

def sqlalchemy_dependency_generator(config: Config) -> Callable[[], AsyncGenerator[Any, Any]]:
		"""
		Returns a function to generate a FastAPI dependency on a SQL Alchemy DB
		"""
		session_local = session_factory(config)

		async def dependency():
				db = session_local()
				try:
						yield db
				finally:
						db.close()

		return dependency