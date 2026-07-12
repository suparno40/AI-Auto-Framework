---
name: ATS Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: critical
execution: before_export
---

# ATS VALIDATOR

## TUJUAN

Validator ini memastikan dokumen dapat dibaca dengan baik oleh Applicant Tracking System (ATS).

Output harus memiliki struktur sederhana, mudah dipindai, dan mengandung kata kunci yang relevan dengan lowongan.

---

# INPUT

{{CV}}

{{CoverLetter}}

{{JobPosting}}

---

# STRUKTUR ATS

Pastikan CV menggunakan heading standar.

Contoh:

- Ringkasan Profesional
- Pengalaman Kerja
- Pendidikan
- Keahlian
- Sertifikasi
- Proyek

---

# KATA KUNCI

Bandingkan isi CV dengan Job Posting.

Pastikan kata kunci penting muncul secara alami.

Contoh:

Operator Produksi

Quality Control

K3

5S

Kaizen

Preventive Maintenance

Troubleshooting

SAP

Microsoft Excel

dan kata kunci lain yang relevan.

Jangan melakukan keyword stuffing.

---

# FORMAT

Pastikan:

- Tidak menggunakan tabel kompleks.
- Tidak menggunakan kolom ganda.
- Tidak menggunakan ikon.
- Tidak menggunakan emoji.
- Tidak menggunakan gambar sebagai informasi utama.
- Tidak menggunakan header/footer yang berisi informasi penting.

---

# FONT DAN TATA LETAK

Gunakan struktur sederhana.

Heading jelas.

Bullet konsisten.

Jarak antarbagian rapi.

---

# BAHASA

Gunakan bahasa yang sesuai dengan lowongan.

Istilah teknis harus konsisten.

---

# LARANGAN

Jangan menggunakan:

★★★★★

★★★★★ Skill Rating

Progress Bar

Icon

SmartArt

WordArt

Grafik

Infografik

---

# VALIDATION CHECKLIST

☐ Heading standar

☐ Keyword sesuai

☐ Tidak ada emoji

☐ Tidak ada ikon

☐ Tidak ada tabel kompleks

☐ Bullet konsisten

☐ Format ATS Friendly

☐ Layout sederhana

---

# HASIL VALIDASI

PASS

Dokumen ramah ATS.

FAIL

Dokumen berpotensi gagal dipindai ATS.

---

# OUTPUT

Jika FAIL,

AI harus memperbaiki struktur hingga memenuhi standar ATS.
