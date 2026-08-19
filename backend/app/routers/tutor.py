from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Dict

from app.db.database import get_db
from app.models.question import Question
from app.services.prompt_templates import build_tutor_system_prompt
from app.services.gemini_client import stream_tutor_reply

router = APIRouter(prefix="/tutor", tags=["tutor"])


class ChatTurn(BaseModel):
    role: str  # "user" หรือ "model"
    text: str


class TutorChatRequest(BaseModel):
    question_id: int
    message: str
    history: List[ChatTurn] = []  # ประวัติแชทก่อนหน้าของข้อนี้ (ถ้ามี)


@router.post("/chat")
async def tutor_chat(payload: TutorChatRequest, db: Session = Depends(get_db)):
    """
    Endpoint หลักของ AI ติวเตอร์รายข้อ
    ส่งคืนเป็น Server-Sent Events (SSE) เพื่อให้ frontend แสดงผลแบบพิมพ์ทีละตัวอักษร

    การเรียกใช้จาก frontend (Next.js) ให้ fetch endpoint นี้แบบ POST
    แล้วอ่าน response.body ผ่าน ReadableStream / EventSource polyfill
    """
    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="ไม่พบโจทย์ข้อนี้")

    system_prompt = build_tutor_system_prompt(question)
    history = [{"role": turn.role, "text": turn.text} for turn in payload.history]

    return StreamingResponse(
        stream_tutor_reply(system_prompt, history, payload.message),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # กันไม่ให้ proxy buffer สตรีม
        },
    )
