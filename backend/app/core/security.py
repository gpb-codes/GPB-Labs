from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            raise ValueError("DATABASE_URL no está definida en el entorno")

        self.DATABASE_URL: str = database_url

settings = Settings()
