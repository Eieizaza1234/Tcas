type ExamFieldCardProps = {
  code: string;          // เช่น "A-LV"
  name: string;          // เช่น "A-Level"
  description: string;
  subjectCount: number;  // จำนวนวิชาที่มีในระบบ (mock data ตอนนี้)
  questionCount: number; // จำนวนข้อสอบสะสม (mock data ตอนนี้)
};

export default function ExamFieldCard({
  code,
  name,
  description,
  subjectCount,
  questionCount,
}: ExamFieldCardProps) {
  return (
    <a
      href="#"
      className="group relative flex flex-col justify-between overflow-hidden rounded-2xl border border-line bg-surface p-6 transition hover:border-signal/60 hover:bg-surfaceHi"
    >
      {/* เส้นประด้านข้างแบบตั๋ว เพื่อสื่อว่านี่คือ 'สนามสอบ' ที่ต้องเลือกเข้าแข่ง */}
      <span className="absolute inset-y-0 left-0 w-1 bg-line transition group-hover:bg-signal" />

      <div className="pl-3">
        <div className="flex items-center justify-between">
          <span className="font-mono text-xs uppercase tracking-widest text-signal">
            {code}
          </span>
          <span className="font-mono text-[11px] text-ink2">
            {questionCount.toLocaleString("th-TH")} ข้อ
          </span>
        </div>

        <h3 className="mt-3 font-display text-xl font-bold text-paper">
          {name}
        </h3>
        <p className="mt-1 text-sm leading-relaxed text-ink2">
          {description}
        </p>
      </div>

      <div className="mt-6 flex items-center justify-between pl-3 font-mono text-xs text-ink2">
        <span>{subjectCount} รายวิชา</span>
        <span className="text-paper opacity-0 transition group-hover:opacity-100">
          เข้าสนาม →
        </span>
      </div>
    </a>
  );
}
