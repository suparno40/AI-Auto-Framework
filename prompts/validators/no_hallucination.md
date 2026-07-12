---
name: No Hallucination Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: critical
execution: after_generation
---

# NO HALLUCINATION VALIDATOR

## TUJUAN

Validator ini bertugas memastikan AI TIDAK membuat informasi yang tidak berasal dari data kandidat maupun data lowongan.

Semua informasi pada output HARUS dapat ditelusuri kembali ke data sumber.

Apabila informasi tidak memiliki sumber yang jelas,

AI WAJIB menghapus informasi tersebut.

---

# INPUT

Gunakan seluruh data yang tersedia.

{{Applicant}}

{{Resume}}

{{CV}}

{{JobPosting}}

{{Company}}

{{HR}}

{{Projects}}

{{Certificates}}

{{Achievements}}

{{Experience}}

{{Education}}

---

# DEFINISI HALLUCINATION

Hallucination adalah informasi yang:

- dibuat AI
- diasumsikan AI
- ditebak AI
- diperkirakan AI
- tidak terdapat pada data sumber

---

# YANG HARUS DICEK

## Identitas

Pastikan:

- Nama
- Email
- Nomor HP
- Alamat
- LinkedIn
- Portfolio

sesuai data sumber.

---

## Pengalaman

Pastikan:

- Nama perusahaan
- Jabatan
- Tahun
- Durasi
- Tugas
- Achievement

identik dengan Resume.

---

## Pendidikan

Pastikan:

- Nama sekolah
- Jurusan
- Tahun
- IPK

tidak berubah.

---

## Sertifikat

Pastikan:

- Nama sertifikat
- Penyelenggara
- Tahun

sesuai data.

Jangan menambahkan sertifikat.

---

## Skill

Pastikan skill benar-benar dimiliki kandidat.

Jangan menambahkan skill baru.

---

## Bahasa

Pastikan bahasa yang disebut memang ada pada data kandidat.

---

## Achievement

Jangan menambahkan:

- peningkatan efisiensi
- pengurangan biaya
- peningkatan produksi
- penghargaan

apabila tidak terdapat pada data sumber.

---

## Angka

Seluruh angka harus divalidasi.

Contoh:

✓ 15%

✓ 3 tahun

✓ 2024

✓ 5 orang

Apabila angka tidak ditemukan pada sumber,

hapus angka tersebut.

---

## Nama Perusahaan

Jangan mengubah nama perusahaan.

Contoh:

PT ABC

tidak boleh menjadi

ABC Corporation

kecuali memang tertulis demikian.

---

## Nama Posisi

Gunakan nama posisi sesuai lowongan.

Jangan membuat nama jabatan baru.

---

## Email HR

Jangan membuat alamat email HR.

Apabila email tidak tersedia,

gunakan sapaan umum.

---

## Nomor Telepon HR

Jangan pernah membuat nomor telepon.

---

## Website

Pastikan website berasal dari sumber.

---

## Produk Perusahaan

Jangan menebak produk perusahaan.

---

## Budaya Perusahaan

Jangan menulis:

"Perusahaan ini memiliki budaya inovatif."

kecuali terdapat pada data perusahaan.

---

## Visi dan Misi

Gunakan hanya apabila tersedia.

---

# ATURAN VALIDASI

Setiap kalimat harus memiliki minimal satu sumber data.

Jika tidak,

hapus kalimat.

---

# LARANGAN

AI TIDAK BOLEH:

- Mengarang pengalaman.
- Mengarang pendidikan.
- Mengarang sertifikat.
- Mengarang angka.
- Mengarang nama HR.
- Mengarang alamat perusahaan.
- Mengarang email.
- Mengarang website.
- Mengarang prestasi.
- Mengarang proyek.
- Mengarang software yang digunakan.
- Mengarang KPI.
- Mengarang gaji.
- Mengarang jabatan.
- Mengarang tanggal.

---

# PENANGANAN DATA KOSONG

Jika informasi tidak tersedia,

gunakan salah satu tindakan berikut:

- Hilangkan bagian tersebut.
- Gunakan kalimat umum tanpa mengarang.
- Jangan membuat placeholder baru.

Contoh:

SALAH

"Saya memiliki sertifikat ISO."

BENAR

Bagian sertifikat dihilangkan.

---

# VALIDATION CHECKLIST

Periksa:

☐ Nama

☐ Email

☐ Nomor HP

☐ Alamat

☐ Pendidikan

☐ Pengalaman

☐ Sertifikat

☐ Skill

☐ Achievement

☐ Tahun

☐ Angka

☐ Nama Perusahaan

☐ Nama Posisi

☐ Bahasa

☐ Website

☐ Email HR

☐ Nomor HR

---

# HASIL VALIDASI

PASS

Semua informasi berasal dari data sumber.

FAIL

Minimal terdapat satu informasi yang tidak memiliki sumber.

---

# OUTPUT

Jika PASS

Lanjutkan ke validator berikutnya.

Jika FAIL

Hapus seluruh informasi yang tidak memiliki sumber,

kemudian lakukan validasi ulang sampai PASS.
