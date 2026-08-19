# TCAS Arena — Backend

Backend สำหรับคลังข้อสอบเข้ามหาวิทยาลัย + ระบบ AI ติวเตอร์ส่วนตัวรายข้อ
สร้างด้วย **FastAPI + SQLite + Gemini API**

## 1. ติดตั้ง

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. ตั้งค่า Gemini API Key

1. ไปที่ https://aistudio.google.com/app/apikey เพื่อขอ API Key (ฟรี)
2. คัดลอก `.env.example` เป็น `.env`
3. ใส่ค่า `GEMINI_API_KEY=` ที่ได้มา

```bash
cp .env.example .env
```

## 3. ใส่ข้อมูลโจทย์ตัวอย่าง (สำหรับทดสอบ)

```bash
python seed_data.py
```

## 4. รันเซิร์ฟเวอร์

```bash
uvicorn app.main:app --reload --port 8000
```

เปิดดู API docs อัตโนมัติได้ที่ **http://localhost:8000/docs**

## Endpoints หลัก

| Method | Path | คำอธิบาย |
|---|---|---|
| GET | `/questions` | ดึงรายการโจทย์ (filter ตาม exam_field/subject/topic) |
| GET | `/questions/random` | สุ่มโจทย์ 1 ข้อ |
| GET | `/questions/{id}` | ดึงโจทย์รายข้อ (ไม่มีเฉลย) |
| GET | `/questions/{id}/answer` | ดึงโจทย์พร้อมเฉลยละเอียด |
| POST | `/tutor/chat` | แชทกับ AI ติวเตอร์ (ตอบกลับแบบ streaming/SSE) |

## ทดสอบ AI ติวเตอร์ด้วย curl

```bash
curl -N -X POST http://localhost:8000/tutor/chat \
  -H "Content-Type: application/json" \
  -d '{"question_id": 1, "message": "ข้อนี้เริ่มทำยังไงดีครับ", "history": []}'
```

จะเห็นข้อความ AI ไหลออกมาทีละ chunk ในรูปแบบ `data: {...}` (SSE)
ซึ่ง Next.js frontend จะนำไปแสดงผลแบบพิมพ์ทีละตัวอักษรต่อไป

## ขั้นตอนถัดไป

- [ ] เชื่อมต่อกับ Next.js frontend (อ่าน stream ด้วย `fetch` + `ReadableStream`)
- [ ] เพิ่มระบบอัปโหลด/จัดการโจทย์จำนวนมาก (import จาก CSV หรือ PDF)
- [ ] เพิ่มระบบผู้ใช้ (login) เพื่อบันทึกประวัติการทำโจทย์
- [ ] ย้ายจาก SQLite ไป PostgreSQL เมื่อพร้อม deploy จริง
