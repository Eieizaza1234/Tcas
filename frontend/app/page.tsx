import Navbar from "@/components/Navbar";
import ExamFieldCard from "@/components/ExamFieldCard";

const examFields = [
  {
    code: "TGAT",
    name: "TGAT",
    description: "ความถนัดทั่วไป: การสื่อสาร การคิดวิเคราะห์ และสมรรถนะการทำงาน",
    subjectCount: 3,
    questionCount: 640,
  },
  {
    code: "TPAT",
    name: "TPAT",
    description: "ความถนัดเฉพาะทาง สายวิศวะ สายแพทย์ สายครุศาสตร์ และอื่นๆ",
    subjectCount: 5,
    questionCount: 890,
  },
  {
    code: "A-LV",
    name: "A-Level",
    description: "วิชาการหลัก คณิต ฟิสิกส์ เคมี ชีววิทยา และภาษา สำหรับยื่นคะแนน",
    subjectCount: 9,
    questionCount: 1520,
  },
  {
    code: "9-วิชา",
    name: "วิชาสามัญ",
    description: "ข้อสอบวิชาสามัญที่มหาวิทยาลัยยังใช้คัดเลือกในบางโครงการ",
    subjectCount: 7,
    questionCount: 410,
  },
];

export default function HomePage() {
  return (
    <>
      <Navbar />

      <main>
        {/* ---------- Hero ---------- */}
        <section className="relative overflow-hidden bg-grid-fade bg-grid">
          <div className="mx-auto flex max-w-6xl flex-col items-start px-6 pb-20 pt-24 md:pt-32">
            <span className="font-mono text-xs uppercase tracking-[0.3em] text-signal">
              คลังข้อสอบเข้ามหาวิทยาลัยยุคใหม่
            </span>

            <h1 className="mt-6 max-w-3xl font-display text-4xl font-bold leading-[1.15] text-paper md:text-6xl">
              ฝึกในสนามซ้อม
              <br />
              ก่อนขึ้นสังเวียนสอบจริง
            </h1>

            <p className="mt-6 max-w-xl text-base leading-relaxed text-ink2 md:text-lg">
              เลือกสนามสอบ วิชา และบทเรียนที่ต้องการฝึก ทำโจทย์จริงพร้อมเฉลยละเอียด
              และคุยกับ AI ติวเตอร์ที่ช่วยคิดตามทีละขั้น ไม่ใช่แค่บอกคำตอบ
            </p>

            <div className="mt-10 flex flex-wrap items-center gap-4">
              <a
                href="#สนามสอบ"
                className="rounded-full bg-signal px-6 py-3 font-display text-sm font-bold text-ink transition hover:brightness-110"
              >
                เลือกสนามสอบ
              </a>
              <a
                href="#ai-tutor"
                className="rounded-full border border-line px-6 py-3 font-display text-sm font-bold text-paper transition hover:border-signal/60"
              >
                ดูระบบ AI ติวเตอร์
              </a>
            </div>

            {/* สกอร์บอร์ดสรุปข้อมูล — องค์ประกอบซิกเนเจอร์ของหน้า */}
            <dl className="mt-16 grid w-full grid-cols-3 gap-6 border-t border-line pt-6 font-mono md:max-w-lg">
              <div>
                <dt className="text-[11px] uppercase tracking-wider text-ink2">
                  สนามสอบ
                </dt>
                <dd className="mt-1 text-2xl font-medium text-paper">4</dd>
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-wider text-ink2">
                  รายวิชา
                </dt>
                <dd className="mt-1 text-2xl font-medium text-paper">24</dd>
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-wider text-ink2">
                  ข้อสอบสะสม
                </dt>
                <dd className="mt-1 text-2xl font-medium text-signal">3,460+</dd>
              </div>
            </dl>
          </div>
        </section>

        {/* ---------- เลือกสนามสอบ ---------- */}
        <section id="สนามสอบ" className="mx-auto max-w-6xl px-6 py-20">
          <div className="mb-10 flex items-end justify-between">
            <div>
              <h2 className="font-display text-2xl font-bold text-paper md:text-3xl">
                เลือกสนามสอบของคุณ
              </h2>
              <p className="mt-2 text-sm text-ink2">
                แต่ละสนามสอบแยกรายวิชาและบทเรียนไว้ให้ครบ พร้อมข้อสอบดาวน์โหลด PDF ได้
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {examFields.map((field) => (
              <ExamFieldCard key={field.code} {...field} />
            ))}
          </div>
        </section>

        {/* ---------- ทีเซอร์ AI ติวเตอร์ ---------- */}
        <section id="ai-tutor" className="border-t border-line bg-surface/40">
          <div className="mx-auto grid max-w-6xl grid-cols-1 items-center gap-12 px-6 py-20 md:grid-cols-2">
            <div>
              <span className="font-mono text-xs uppercase tracking-[0.3em] text-wave">
                AI ติวเตอร์ส่วนตัว
              </span>
              <h2 className="mt-4 font-display text-2xl font-bold text-paper md:text-3xl">
                ติดตรงไหน ถามได้ทันทีในข้อนั้นเลย
              </h2>
              <p className="mt-4 text-sm leading-relaxed text-ink2 md:text-base">
                AI ติวเตอร์จะไม่บอกเฉลยทันที แต่จะค่อยๆ ตั้งคำถามชวนคิด
                จนกว่าคุณจะเข้าใจวิธีทำเอง — เหมือนมีพี่ติวนั่งข้างๆ ทุกข้อ
              </p>
            </div>

            {/* กล่องแชทจำลอง แสดง concept การพิมพ์ทีละตัวอักษร (ยังไม่ทำงานจริงในหน้านี้) */}
            <div className="rounded-2xl border border-line bg-ink p-5">
              <div className="flex items-center gap-2 border-b border-line pb-3">
                <span className="h-2 w-2 rounded-full bg-wave" />
                <span className="font-mono text-xs uppercase tracking-wider text-ink2">
                  AI ติวเตอร์ · คณิต 1
                </span>
              </div>
              <div className="mt-4 space-y-3 text-sm">
                <p className="max-w-[85%] rounded-xl rounded-tl-none bg-surface px-4 py-2 text-paper">
                  ลองดูก่อนว่าเวกเตอร์ AB หาได้จากอะไร ระหว่างจุด A กับ B ครับ?
                </p>
                <p className="ml-auto max-w-[85%] rounded-xl rounded-tr-none bg-signal/90 px-4 py-2 text-ink">
                  เอาจุด B ลบ จุด A ใช่ไหมครับ
                </p>
                <p className="max-w-[85%] rounded-xl rounded-tl-none bg-surface px-4 py-2 text-paper">
                  ถูกต้อง<span className="animate-pulse text-ink2">▊</span>
                </p>
              </div>
            </div>
          </div>
        </section>

        <footer className="border-t border-line px-6 py-10">
          <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 font-mono text-xs text-ink2 md:flex-row">
            <span>© 2026 TCAS Arena</span>
            <span>สร้างเพื่อการศึกษา ไม่มีส่วนเกี่ยวข้องกับ ทปอ.</span>
          </div>
        </footer>
      </main>
    </>
  );
}
