"""
สคริปต์ใส่ข้อมูลโจทย์ตัวอย่างลงฐานข้อมูล เพื่อใช้ทดสอบระบบ
วิธีใช้: python seed_data.py  (รันจากโฟลเดอร์ backend/)
"""
from app.db.database import SessionLocal, Base, engine
from app.models.question import Question

Base.metadata.create_all(bind=engine)

sample_questions = [
    Question(
        exam_field="A-Level",
        subject="คณิต 1",
        topic="เวกเตอร์",
        difficulty="medium",
        question_text="กำหนดให้ A(1, 2) และ B(4, 6) จงหาขนาดของเวกเตอร์ AB",
        choices=["ก. 3", "ข. 4", "ค. 5", "ง. 7"],
        correct_answer="ค. 5",
        explanation=(
            "เวกเตอร์ AB = B - A = (4-1, 6-2) = (3, 4)\n"
            "ขนาด = √(3² + 4²) = √(9+16) = √25 = 5"
        ),
    ),
    Question(
        exam_field="A-Level",
        subject="ฟิสิกส์",
        topic="การเคลื่อนที่แนวตรง",
        difficulty="easy",
        question_text="วัตถุเคลื่อนที่ด้วยความเร็วต้น 0 m/s ความเร่งคงที่ 2 m/s² "
        "หลังจากเวลา 5 วินาที วัตถุเคลื่อนที่ได้ระยะทางเท่าใด",
        choices=["ก. 10 m", "ข. 20 m", "ค. 25 m", "ง. 50 m"],
        correct_answer="ค. 25 m",
        explanation=(
            "ใช้สูตร s = ut + ½at²\n"
            "s = (0)(5) + ½(2)(5²) = 0 + ½(2)(25) = 25 m"
        ),
    ),
    Question(
        exam_field="TGAT",
        subject="เคมี",
        topic="โครงสร้างอะตอม",
        difficulty="easy",
        question_text="ธาตุ X มีเลขอะตอม 11 จัดเรียงอิเล็กตรอนแบบใด",
        choices=["ก. 2, 8, 1", "ข. 2, 8, 2", "ค. 2, 9", "ง. 1, 8, 2"],
        correct_answer="ก. 2, 8, 1",
        explanation=(
            "เลขอะตอม 11 หมายถึงมี 11 อิเล็กตรอน จัดเรียงตามระดับพลังงาน "
            "K(2), L(8), M(1) รวมเป็น 2+8+1 = 11"
        ),
    ),
]

db = SessionLocal()
try:
    db.add_all(sample_questions)
    db.commit()
    print(f"เพิ่มโจทย์ตัวอย่างสำเร็จ {len(sample_questions)} ข้อ")
finally:
    db.close()
