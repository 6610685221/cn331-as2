# cn331-as2
## เนตรชนก ยินดี 6610685221
# ระบบจองห้องเรียน (Classroom Booking System)

[classroom-booking web](https://cn331-as2-905l.onrender.com)
[คลิปวิดีโอสาธิต classroom-booking บน clound](https://youtu.be/x3lM5A9UqMc)
**Classroom Booking System** เป็นเว็บแอปพลิเคชันที่พัฒนาขึ้นด้วย Django Framework สำหรับจัดการและจองห้องเรียนออนไลน์ ผู้ใช้ทั่วไปสามารถสมัครสมาชิก, ค้นหาห้องที่ต้องการ, และทำการจองห้องที่ยังว่างอยู่ได้ ในขณะที่ผู้ดูแลระบบสามารถจัดการข้อมูลห้องทั้งหมดได้อย่างง่ายดาย

## คุณสมบัติหลัก (Key Features)

- **ระบบยืนยันตัวตน:** สมัครสมาชิก, เข้าสู่ระบบ, ออกจากระบบ
- **การค้นหา:** ค้นหาห้องเรียนจาก "ชื่อห้อง" หรือ "รหัสห้อง"
- **ระบบการจอง:** ผู้ใช้ที่ล็อกอินแล้วสามารถจองและยกเลิกการจองห้องได้
- **การจัดการการจอง:** หน้า "My Bookings" สำหรับดูรายการจองส่วนตัว
- **ระบบจัดการสำหรับ Admin:** สร้าง, แก้ไข, ลบข้อมูลห้อง (CRUD) และดูรายชื่อผู้ที่จองห้องได้
- **ข้อความแจ้งเตือน:** แสดงผลการทำงานต่างๆ เช่น จองสำเร็จ, ยกเลิกสำเร็จ, หรือเกิดข้อผิดพลาด

## เทคโนโลยีที่ใช้ (Technology Stack)

- **Backend:** Python, Django Framework
- **Frontend:** HTML, CSS
- **Database:** SQLite

---

## โครงสร้างโปรเจกต์ (Project Structure)

โครงสร้างของโปรเจกต์ถูกจัดระเบียบตามมาตรฐานของ Django เพื่อให้ง่ายต่อการพัฒนาและดูแลรักษา

```classroom_booking/
│
├── .venv/                   # โฟลเดอร์ Virtual Environment
├── booking/                 # Django App หลักของระบบจอง
│   ├── migrations/          # ไฟล์สำหรับจัดการการเปลี่ยนแปลงของ Database
│   ├── templates/booking/   # เก็บไฟล์ HTML ที่ใช้เฉพาะในแอป booking
│   │   ├── cancel_booking.html
│   │   ├── delete.html
│   │   ├── home.html
│   │   ├── login_register.html
│   │   ├── room_booking.html
│   │   ├── room_form.html
│   │   ├── room.html
│   │   └── schedule.html
│   ├── admin.py             # ลงทะเบียน Models เพื่อแสดงในหน้า Admin
│   ├── apps.py              # ตั้งค่าของแอป booking
│   ├── forms.py             # กำหนดฟอร์มที่ใช้ (เช่น ฟอร์มสร้างห้อง)
│   ├── models.py            # กำหนดโครงสร้างของ Database (ตาราง Room, Booking)
│   ├── urls.py              # กำหนด URL Paths ของแอป booking
│   └── views.py             # โค้ดหลักที่จัดการ Logic และการแสดงผลของแอป
│
├── classroom_booking/       # โฟลเดอร์หลักสำหรับตั้งค่าโปรเจกต์
│   ├── settings.py          # ไฟล์ตั้งค่าหลักของโปรเจกต์ทั้งหมด
│   ├── urls.py              # ไฟล์ URL หลักที่เชื่อมไปยังแอปต่างๆ
│   └── ...
│
├── static/                  # โฟลเดอร์เก็บไฟล์ CSS, JavaScript, รูปภาพ
│   ├── images/
│   └── styles/
│       └── main.css         # ไฟล์ CSS หลักสำหรับตกแต่งเว็บ
│
├── templates/               # โฟลเดอร์เก็บไฟล์ HTML ที่ใช้ร่วมกันทั้งโปรเจกต์
│   ├── main.html            # Template โครงสร้างหลักของทุกหน้า
│   └── navbar.html          # Template ของแถบเมนูด้านบน
│
├── db.sqlite3               # ไฟล์ฐานข้อมูล SQLite
├── manage.py                # เครื่องมือสำหรับรันคำสั่งต่างๆ ของ Django
└── README.md                # ไฟล์เอกสารอธิบายโปรเจกต์ (ไฟล์นี้)
