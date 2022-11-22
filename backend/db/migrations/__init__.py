import os

from alembic import command as alembic
from alembic.config import Config
from config import config


def get_alembic_config() -> Config:
    alembic_cfg = Config()
    script_location = (
        "db/migrations" if os.getenv("ENV") == "local" else "db/migrations"
    )
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", str(config.postgres_url()))
    return alembic_cfg


def apply_migrations() -> None:
    alembic_cfg = get_alembic_config()
    alembic.upgrade(alembic_cfg, "head")