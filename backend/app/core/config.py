import os


class Settings:
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://logsmith_user:logsmith_password@localhost:5433/logsmith",
    )


settings = Settings()