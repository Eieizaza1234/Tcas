from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.db.database import Base, engine
from app.routers import questions, tutor

# สร้างตารางในฐานข้อมูลถ้ายังไม่มี (สำหรับ SQLite/dev)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TCAS Arena API",
    description="Backend สำหรับคลังข้อสอบเข้ามหาวิทยาลัย และระบบ AI ติวเตอร์ส่วนตัว",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router)
app.include_router(tutor.router)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "TCAS Arena API"}
