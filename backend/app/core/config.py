from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL: str

    def __init__(self) -> None:
        database_url = os.getenv("DATABASE_URL")

        if database_url is None:
            raise RuntimeError(
                "DATABASE_URL no está definida. Revisa el archivo .env"
            )

        self.DATABASE_URL = database_url


settings = Settings()
