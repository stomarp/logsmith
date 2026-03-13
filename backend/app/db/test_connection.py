from sqlalchemy import text

from app.db.base import engine


def test_db_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful:", result.scalar())


if __name__ == "__main__":
    test_db_connection()