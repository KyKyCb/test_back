from enum import Enum
from pathlib import Path
import environ

env_path = Path('.env').resolve()
print(env_path)
env = environ.Env()
env.read_env(env_path)


class EnvironmentList(Enum):
    development = "development"
    production = "production"


DB_NAME = env("PGDATABASE")
DB_USER = env("PGUSER")
DB_PASSWORD = env("PGPASSWORD")
DB_HOST = env("PGHOST")
DB_PORT = env("PGPORT")

SECRET_KEY: str = env("SECRET_KEY")
ENV_VAR: str = env("ENVIRONMENT")