export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-line/60 bg-ink/80 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <a href="/" className="flex items-baseline gap-2 font-display">
          <span className="text-lg font-bold tracking-tight text-paper">
            TCAS<span className="text-signal">ARENA</span>
          </span>
        </a>

        <nav className="hidden items-center gap-8 font-mono text-xs uppercase tracking-wider text-ink2 md:flex">
          <a href="#สนามสอบ" className="transition hover:text-paper">
            สนามสอบ
          </a>
          <a href="#" className="transition hover:text-paper">
            คลังข้อสอบ
          </a>
          <a href="#" className="transition hover:text-paper">
            AI ติวเตอร์
          </a>
        </nav>

        <button
          type="button"
          disabled
          title="ระบบสมาชิกกำลังพัฒนา"
          className="rounded-full border border-line px-4 py-1.5 font-mono text-xs uppercase tracking-wider text-ink2 opacity-60"
        >
          เข้าสู่ระบบ
        </button>
      </div>
    </header>
  );
}
