from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from typing import Optional, List

from app.db.database import get_db
from app.models.question import Question, QuestionOut, QuestionWithAnswer

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("", response_model=List[QuestionOut])
def list_questions(
    exam_field: Optional[str] = None,
    subject: Optional[str] = None,
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    limit: int = Query(default=20, le=100),
    db: Session = Depends(get_db),
):
    """ดึงรายการโจทย์ พร้อม filter ตามสนามสอบ/วิชา/บทเรียน/ความยาก"""
    q = db.query(Question)
    if exam_field:
        q = q.filter(Question.exam_field == exam_field)
    if subject:
        q = q.filter(Question.subject == subject)
    if topic:
        q = q.filter(Question.topic == topic)
    if difficulty:
        q = q.filter(Question.difficulty == difficulty)
    return q.limit(limit).all()


@router.get("/random", response_model=QuestionOut)
def get_random_question(
    subject: Optional[str] = None,
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """สุ่มโจทย์ 1 ข้อ ตามเงื่อนไขที่กำหนด (ใช้สำหรับปุ่ม 'สุ่มโจทย์ทำ')"""
    q = db.query(Question)
    if subject:
        q = q.filter(Question.subject == subject)
    if topic:
        q = q.filter(Question.topic == topic)
    if difficulty:
        q = q.filter(Question.difficulty == difficulty)

    question = q.order_by(func.random()).first()
    if not question:
        raise HTTPException(status_code=404, detail="ไม่พบโจทย์ที่ตรงกับเงื่อนไข")
    return question


@router.get("/{question_id}", response_model=QuestionOut)
def get_question(question_id: int, db: Session = Depends(get_db)):
    """ดึงโจทย์รายข้อ (ไม่รวมเฉลย)"""
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="ไม่พบโจทย์ข้อนี้")
    return question


@router.get("/{question_id}/answer", response_model=QuestionWithAnswer)
def get_question_answer(question_id: int, db: Session = Depends(get_db)):
    """ดึงโจทย์พร้อมเฉลย (ใช้ตอนผู้ใช้กด 'เฉลยละเอียด')"""
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="ไม่พบโจทย์ข้อนี้")
    return question
