# Novel Project

Project นี้ใช้สำหรับจัดการนิยายและ Bible โดยทำงานร่วมกับ AI (Gemini)

## Credit

This project was developed with assistance from GitHub Copilot for brainstorming, structure, drafting support, and iterative revision.

## โครงสร้างโปรเจกต์

```
Novel/
├── bible/
│   ├── images/          # Bible ต้นฉบับในรูปแบบภาพ (source/reference)
│   ├── characters/      # ข้อมูลตัวละครสำหรับ AI อ้างอิง
│   ├── world/           # ข้อมูลโลก กฎ ระบบ และ lore
│   ├── locations/       # ข้อมูลสถานที่
│   ├── factions/        # กลุ่ม องค์กร และฝ่ายต่าง ๆ
│   ├── relationships/   # ความสัมพันธ์ระหว่างตัวละครและกลุ่ม
│   └── timeline/        # เหตุการณ์และ timeline ที่เป็น canon
│
├── plot/
│   ├── premise/         # premise และแนวคิดหลักของเรื่อง
│   ├── arcs/            # story arcs และโครงเรื่องระดับใหญ่
│   └── chapter-plans/   # แผนของแต่ละ chapter ก่อนเริ่มเขียนจริง
│
├── chapters/            # นิยายฉบับเขียนจริง แยกเป็น chapter
│
├── notes/
│   ├── ideas/           # ไอเดียที่ยังไม่ถือเป็น canon
│   ├── research/        # ข้อมูลค้นคว้าและ reference
│   └── unresolved/      # ประเด็นที่ยังตัดสินใจไม่ได้
│
└── .kiro/
    └── steering/        # กฎและบริบทถาวรสำหรับ Kiro Agent
```
