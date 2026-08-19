import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./tcas_arena.db")


settings = Settings()

if not settings.GEMINI_API_KEY:
    print(
        "[WARNING] ยังไม่ได้ตั้งค่า GEMINI_API_KEY ใน .env — "
        "ระบบ AI ติวเตอร์จะยังใช้งานไม่ได้จนกว่าจะใส่ API Key "
        "(ขอได้ที่ https://aistudio.google.com/app/apikey)"
    )
