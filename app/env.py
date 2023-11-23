import os

DATABASE = os.getenv("DATABASE", "Base_ADBD")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
DATABASE_USER = os.getenv("DATABASE_USER", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "admin")
