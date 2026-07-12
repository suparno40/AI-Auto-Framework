---
name: Placeholder Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: critical
execution: after_generation
---

# PLACEHOLDER VALIDATOR

## TUJUAN

Validator ini memastikan tidak ada placeholder template yang tersisa pada dokumen akhir.

Output HARUS siap dikirim kepada HR tanpa memuat variabel template.

---

# PLACEHOLDER YANG HARUS DICEK

Contoh placeholder:

{{Name}}

{{FullName}}

{{Company}}

{{Position}}

{{Email}}

{{Phone}}

{{Address}}

{{LinkedIn}}

{{Portfolio}}

{{Date}}

{{Skills}}

{{Experience}}

{{Education}}

{{Certificates}}

{{Projects}}

{{Achievements}}

dan seluruh placeholder lain yang menggunakan format:

{{...}}

---

# ATURAN

AI HARUS memindai seluruh dokumen.

Jika ditemukan placeholder,

validator langsung FAIL.

---

# PENANGANAN

Jika data tersedia

→ Ganti placeholder dengan data sebenarnya.

Jika data tidak tersedia

→ Hapus kalimat tersebut.

Jangan meninggalkan placeholder.

---

# LARANGAN

JANGAN menghasilkan:

{{Company}}

{{Position}}

{{Name}}

N/A

Unknown

Lorem Ipsum

TBD

Coming Soon

-

NULL

None

---

# VALIDATION CHECKLIST

☐ Tidak ada {{ }}

☐ Tidak ada []

☐ Tidak ada <placeholder>

☐ Tidak ada TBD

☐ Tidak ada Lorem Ipsum

☐ Tidak ada Unknown

☐ Tidak ada N/A

---

# OUTPUT

PASS

Tidak ditemukan placeholder.

FAIL

Masih terdapat placeholder.

Apabila FAIL,

AI wajib mengganti atau menghapus placeholder sebelum dokumen dinyatakan selesai.
