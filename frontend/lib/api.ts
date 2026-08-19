// จุดรวมค่า config สำหรับเรียก backend (FastAPI)
// ตอนนี้ยังไม่มีหน้าไหนเรียกใช้จริง เตรียมไว้สำหรับหน้าคลังข้อสอบ/AI ติวเตอร์ที่จะทำต่อ

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
