import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    SQLALCHEMY_DATABASE_URI = (
        DATABASE_URL or f"sqlite:///{os.path.join(basedir, 'app.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SES_REGION_NAME = os.environ.get("SES_REGION_NAME")
    SES_REGION_SOURCE = os.environ.get("SES_REGION_SOURCE")

    ADMINS = [os.environ.get("ADMIN_EMAIL")]

    POSTS_PER_PAGE = 25

    LANGUAGES = ["en", "fr"]

    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")

    ELASTICSEARCH_URL = os.environ.get("ELASTICSEARCH_URL")

    REDIS_URL = os.environ.get("REDIS_URL") or "redis://"

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
