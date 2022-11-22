import os

if os.path.exists("env"):
		for filename in os.listdir("env"):
				if filename.endswith(".default"):
						with open(f"env/{filename}", "r") as file:
								os.environ[filename.split(".default")[0]] = file.read()


class Config():
		"""
		Your application's configuration, based on pydantic's BaseSettings.
		See doc at https://pydantic-docs.helpmanual.io/usage/settings/
		You can add your config parameters here, together with whatever
		custom parsing & validation might be necessary.
		"""

		POSTGRES_USER = os.environ.get("POSTGRES_USER")
		POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
		POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
		POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
		POSTGRES_DB = "next-fast-postgres-template"
		SERVICE_NAME = "next-fast-postgres-template"


		def postgres_url(self) -> str:
			return "postgresql://nfp_user:password@localhost:5432/next-fast-postgres-template"
				# return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'