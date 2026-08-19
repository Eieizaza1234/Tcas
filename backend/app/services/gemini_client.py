import json
from typing import AsyncGenerator, List, Dict
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def _build_model(system_prompt: str):
    return genai.GenerativeModel(
        model_name=settings.GEMINI_MODEL,
        system_instruction=system_prompt,
    )


async def stream_tutor_reply(
    system_prompt: str,
    chat_history: List[Dict[str, str]],
    user_message: str,
) -> AsyncGenerator[str, None]:
    """
    เรียก Gemini API แบบ stream และ yield ข้อความออกมาทีละ chunk
    ในรูปแบบ Server-Sent Events (SSE) เพื่อให้ frontend แสดงผลแบบพิมพ์ทีละตัวอักษร

    chat_history: [{"role": "user"/"model", "text": "..."}]
    """
    if not settings.GEMINI_API_KEY:
        yield _sse_event({"error": "ยังไม่ได้ตั้งค่า GEMINI_API_KEY บน server"})
        return

    model = _build_model(system_prompt)

    # แปลง history ให้ตรงกับ format ของ google-generativeai
    formatted_history = [
        {"role": turn["role"], "parts": [turn["text"]]} for turn in chat_history
    ]

    chat = model.start_chat(history=formatted_history)

    try:
        response = chat.send_message(user_message, stream=True)
        for chunk in response:
            if chunk.text:
                yield _sse_event({"delta": chunk.text})
        yield _sse_event({"done": True})
    except Exception as e:
        yield _sse_event({"error": f"เกิดข้อผิดพลาดขณะเรียก Gemini API: {str(e)}"})


def _sse_event(data: dict) -> str:
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
