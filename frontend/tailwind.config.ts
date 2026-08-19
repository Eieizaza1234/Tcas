import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#0B1120",      // พื้นหลังหลัก โทนกลางคืนของสนามสอบ
        surface: "#131B2E",   // การ์ด/พื้นผิวลอย
        surfaceHi: "#1B2540", // การ์ดตอน hover
        line: "#26314D",      // เส้นแบ่ง/ขอบ
        ink2: "#8B93A7",       // ตัวอักษรรอง
        paper: "#E7EAF0",      // ตัวอักษรหลักบนพื้นเข้ม
        signal: "#F5B400",     // สีไฟสปอตไลท์ — accent หลัก (ปุ่ม, ไฮไลต์)
        signalDim: "#7A5C00",
        wave: "#2DD4BF",       // สีรองสำหรับแท็กวิชา/สถานะ
      },
      fontFamily: {
        display: ["var(--font-display)", "sans-serif"],
        body: ["var(--font-body)", "sans-serif"],
        mono: ["var(--font-mono)", "monospace"],
      },
      backgroundImage: {
        "grid-fade":
          "linear-gradient(to bottom, rgba(11,17,32,0) 0%, #0B1120 85%), radial-gradient(circle at 1px 1px, #26314D 1px, transparent 0)",
      },
      backgroundSize: {
        grid: "100% 100%, 28px 28px",
      },
    },
  },
  plugins: [],
};

export default config;
