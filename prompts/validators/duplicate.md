---
name: Duplicate Content Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: medium
execution: before_export
---

# DUPLICATE VALIDATOR

## TUJUAN

Mendeteksi informasi yang ditulis berulang.

---

# PERIKSA

- Kalimat sama
- Bullet sama
- Skill berulang
- Achievement berulang
- Pengalaman berulang
- Paragraf berulang

---

# ATURAN

Setiap informasi cukup ditulis satu kali.

Jika ditemukan duplikasi,

hapus versi yang kurang relevan.

---

# OUTPUT

PASS

Tidak ditemukan duplikasi.

FAIL

Hilangkan seluruh informasi yang berulang.
