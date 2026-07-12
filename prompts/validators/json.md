---
name: JSON Validator
version: 4.0
author: AI-Auto-Framework
type: validator
priority: medium
execution: before_export
---

# JSON VALIDATOR

## TUJUAN

Memastikan seluruh output JSON valid.

---

# PERIKSA

- UTF-8
- Valid JSON
- Tidak ada trailing comma
- Tidak ada duplicate key
- Tidak ada key kosong
- Tidak ada value null yang tidak diperlukan

---

# FORMAT

Gunakan:

Object

Array

String

Boolean

Number

sesuai standar JSON.

---

# VALIDATION CHECKLIST

☐ Valid JSON

☐ UTF-8

☐ Tidak ada trailing comma

☐ Tidak ada duplicate key

☐ Struktur benar

---

# OUTPUT

PASS

JSON valid.

FAIL

Perbaiki struktur JSON.
