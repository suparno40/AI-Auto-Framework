---
name: Factual Consistency Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: critical
execution: after_generation
---

# FACTUAL CONSISTENCY VALIDATOR

## TUJUAN

Validator ini memastikan seluruh dokumen yang dihasilkan AI memiliki fakta yang konsisten.

Semua data pada:

- CV
- Cover Letter
- Email
- Resume
- JSON Output

harus saling sesuai.

Tidak boleh ada informasi yang bertentangan.

---

# INPUT

Gunakan seluruh dokumen yang telah dibuat.

{{Resume}}

{{CV}}

{{CoverLetter}}

{{Email}}

{{Applicant}}

{{JobPosting}}

{{Company}}

---

# YANG HARUS DICEK

## IDENTITAS

Pastikan sama pada seluruh dokumen.

- Nama
- Email
- Nomor HP
- Alamat
- LinkedIn
- Portfolio

---

## POSISI

Pastikan posisi yang dilamar identik.

Contoh

CV

Operator Produksi

Cover Letter

Operator Produksi

Email

Operator Produksi

Jangan sampai berubah menjadi

Operator Warehouse

Operator Mesin

Production Staff

apabila bukan nama posisi sebenarnya.

---

## PERUSAHAAN

Pastikan seluruh dokumen menggunakan nama perusahaan yang sama.

Jangan menyingkat.

Jangan menerjemahkan.

---

## TAHUN

Pastikan:

- tahun kerja
- tahun pendidikan
- tahun sertifikat

identik.

---

## DURASI

Pastikan:

3 Tahun

tetap

3 Tahun

Jangan berubah menjadi

4 Tahun

---

## JABATAN

Pastikan nama jabatan sama.

---

## SKILL

Skill yang muncul pada Cover Letter

harus tersedia pada CV.

---

## PENGALAMAN

Pastikan seluruh pengalaman yang disebut benar-benar ada.

---

## ACHIEVEMENT

Achievement pada Cover Letter

harus berasal dari CV.

---

## ANGKA

Semua angka harus sama.

Contoh

20%

5 Orang

2024

Zero Accident

ISO 9001

---

## PENDIDIKAN

Pastikan:

Sekolah

Jurusan

IPK

Tahun

identik.

---

## SERTIFIKAT

Nama sertifikat

Penyelenggara

Tahun

harus sama.

---

## KONTAK

Nomor HP

Email

LinkedIn

tidak boleh berbeda.

---

# PENYESUAIAN LOWONGAN

AI boleh mengubah urutan informasi.

AI TIDAK BOLEH mengubah fakta.

---

# PERBEDAAN YANG DIPERBOLEHKAN

AI boleh:

- Meringkas
- Mengubah gaya bahasa
- Mengubah urutan paragraf
- Menghapus informasi yang tidak relevan

AI tidak boleh:

- Menambah fakta baru
- Mengubah angka
- Mengubah tahun
- Mengubah jabatan
- Mengubah nama perusahaan

---

# LARANGAN

AI TIDAK BOLEH:

Mengganti fakta.

Mengubah tanggal.

Mengubah angka.

Mengubah nama perusahaan.

Mengubah nama kandidat.

Mengubah sertifikat.

Mengubah pendidikan.

Mengubah pengalaman.

---

# VALIDATION CHECKLIST

☐ Nama sama

☐ Email sama

☐ Nomor HP sama

☐ Posisi sama

☐ Nama perusahaan sama

☐ Tahun sama

☐ Durasi sama

☐ Pengalaman sama

☐ Skill sama

☐ Achievement sama

☐ Pendidikan sama

☐ Sertifikat sama

☐ Bahasa konsisten

---

# HASIL VALIDASI

PASS

Seluruh dokumen konsisten.

FAIL

Minimal terdapat satu fakta yang berbeda.

---

# OUTPUT

Jika PASS

Lanjutkan validator berikutnya.

Jika FAIL

Sinkronkan seluruh dokumen.

Lakukan validasi ulang hingga PASS.
