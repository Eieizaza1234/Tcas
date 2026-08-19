from sqlalchemy import Column, Integer, String, Text, JSON
from pydantic import BaseModel
from typing import Optional, List
from app.db.database import Base


# ---------- SQLAlchemy Model (โครงสร้างตาราง) ----------
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    exam_field = Column(String, index=True)      # สนามสอบ เช่น "TGAT", "A-Level"
    subject = Column(String, index=True)         # รายวิชา เช่น "คณิต 1", "ฟิสิกส์"
    topic = Column(String, index=True)           # บทเรียน เช่น "เวกเตอร์", "การเคลื่อนที่"
    difficulty = Column(String, default="medium")  # easy / medium / hard

    question_text = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)     # รูปประกอบโจทย์ (ถ้ามี)

    choices = Column(JSON, nullable=True)          # ["ก. ...", "ข. ...", "ค. ...", "ง. ..."]
    correct_answer = Column(String, nullable=False)  # เช่น "ข"
    explanation = Column(Text, nullable=False)      # เฉลยละเอียด

    pdf_source_url = Column(String, nullable=True)  # ลิงก์ไฟล์ PDF ต้นฉบับ (ถ้ามี)


# ---------- Pydantic Schemas (สำหรับ API request/response) ----------
class QuestionOut(BaseModel):
    id: int
    exam_field: str
    subject: str
    topic: str
    difficulty: str
    question_text: str
    image_url: Optional[str] = None
    choices: Optional[List[str]] = None
    # หมายเหตุ: ตอนแสดงโจทย์ให้ผู้ใช้ทำ ไม่ควรส่ง correct_answer / explanation ไปด้วย
    # จะส่งให้ก็ต่อเมื่อผู้ใช้ตอบแล้ว หรือกดขอเฉลย

    class Config:
        from_attributes = True


class QuestionWithAnswer(QuestionOut):
    correct_answer: str
    explanation: str


class QuestionCreate(BaseModel):
    exam_field: str
    subject: str
    topic: str
    difficulty: str = "medium"
    question_text: str
    image_url: Optional[str] = None
    choices: Optional[List[str]] = None
    correct_answer: str
    explanation: str
    pdf_source_url: Optional[str] = None
