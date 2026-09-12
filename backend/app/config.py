import os


def _require_env(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"{name} environment variable is not set — see backend/.env.example"
        )
    return value


class Config:
    SECRET_KEY = _require_env("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = _require_env("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
