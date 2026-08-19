# TCAS Arena — Frontend (โครงเริ่มต้น)

Next.js 14 (App Router) + TypeScript + Tailwind CSS

ตอนนี้มีแค่ **หน้าแรก (Home)** ตามที่ขอไว้ ยังไม่เชื่อมกับ backend จริง
(การ์ดสนามสอบและตัวเลขสถิติเป็น mock data ทั้งหมด)

## ติดตั้งและรัน

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

เปิดดูที่ **http://localhost:3000**

## โครงสร้างไฟล์

```
frontend/
├── app/
│   ├── layout.tsx     # โหลดฟอนต์ + metadata ของเว็บ
│   ├── page.tsx        # หน้าแรก (Home)
│   └── globals.css     # Tailwind base + focus ring + reduced motion
├── components/
│   ├── Navbar.tsx
│   └── ExamFieldCard.tsx
├── lib/
│   └── api.ts           # ตั้งค่า URL เรียก backend (เตรียมไว้ ยังไม่ใช้จริง)
└── tailwind.config.ts   # โทนสี/ฟอนต์เฉพาะของ TCAS Arena
```

## แนวคิดการออกแบบ

- โทนสี "สนามยามค่ำคืน": พื้นหลังกรมท่าเข้ม (`ink`) + สีไฟสปอตไลท์เหลืองอำพัน (`signal`)
  เป็น accent หลัก สื่อถึงบรรยากาศ "สนามแข่ง/Arena"
- การ์ดเลือกสนามสอบออกแบบให้คล้าย "ตั๋วเข้าแข่ง" มีรหัสสนามสอบ, จำนวนข้อสอบ,
  เส้นขอบซ้ายที่ติดไฟตอน hover
- ฟอนต์: Space Grotesk (หัวข้อ) + IBM Plex Sans Thai (เนื้อหา) + IBM Plex Mono (ตัวเลข/label)

## ขั้นตอนถัดไป (ยังไม่ได้ทำในรอบนี้)

- [ ] หน้าคลังข้อสอบ (`/questions`) พร้อม filter เชื่อมกับ `GET /questions`
- [ ] หน้าทำโจทย์รายข้อ + แชท AI ติวเตอร์ เชื่อมกับ `POST /tutor/chat`
      (ต้องอ่าน response แบบ stream ด้วย `fetch` + `ReadableStream` เพื่อให้ขึ้นทีละตัวอักษร)
- [ ] หน้า Login/สมัครสมาชิก
