import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "mysql://seaport_user:Admin%401234@localhost/seaport_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
