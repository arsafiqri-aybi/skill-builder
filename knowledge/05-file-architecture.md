## 5. Spesifikasi dan arsitektur berkas

### 5.1 Bentuk minimum

~~~text
ai-skill-architect/
└── SKILL.md
~~~

Isi minimum:

~~~yaml
---
name: ai-skill-architect
description: Rancang, tinjau, dan uji Skill ChatGPT dari kebutuhan nyata. Gunakan saat pengguna meminta pembuatan atau perbaikan Skill dan evaluasi pemicunya.
---

Instruksi kerja Skill di sini.
~~~

Spesifikasi terbuka mewajibkan **SKILL.md** dengan YAML frontmatter; **name** harus cocok dengan nama folder, memakai huruf kecil ASCII, angka, dan tanda hubung, maksimal 64 karakter; **description** berisi fungsi dan kapan Skill digunakan, maksimal 1.024 karakter. Deskripsi singkat dan spesifik biasanya lebih berguna daripada mendekati batas maksimum. Detail validasi dapat berbeda antar lingkungan; pakai aturan lingkungan tujuan ketika memasang. [S2][S3]

### 5.2 Komponen tambahan bila perlu

~~~text
ai-skill-architect/
├── SKILL.md
├── references/
│   └── pedoman-validasi.md
├── scripts/
│   └── periksa-skill.py
├── assets/
│   └── contoh-template.md
└── agents/
    └── openai.yaml
~~~

| Lokasi | Peran | Tambahkan jika |
| --- | --- | --- |
| SKILL.md | Metadata pemicu dan alur inti | Selalu ada |
| references/ | Standar, skema, kebijakan, pedoman domain | Detail panjang dan hanya kadang relevan |
| scripts/ | Perhitungan atau pemrosesan berulang yang membutuhkan hasil deterministik | Instruksi saja terbukti kurang andal |
| assets/ | Templat, desain, atau bahan yang menjadi bagian dari keluaran | Ada berkas yang memang harus dipakai ulang |
| agents/openai.yaml | Metadata tampilan dan, pada lingkungan yang mendukung, kebijakan pemanggilan serta dependensi alat | Antarmuka atau integrasi membutuhkannya |

Struktur itu didukung panduan OpenAI dan spesifikasi terbuka. Bidang tambahan dalam spesifikasi terbuka tidak berarti setiap platform akan memakainya; misalnya **allowed-tools** ditandai eksperimental. Hindari bergantung kepadanya tanpa uji pada lingkungan tujuan. [S2][S3]

### 5.3 Prinsip pemuatan bertahap

- **Metadata:** nyatakan pekerjaan dan kondisi pemicu sesingkat mungkin.
- **SKILL.md:** simpan langkah esensial, aturan keputusan, batas keselamatan, dan definisi selesai.
- **Referensi:** simpan materi besar yang hanya dibutuhkan untuk cabang tugas tertentu.
- **Skrip:** jalankan fungsi deterministik; dokumentasikan input/output dan dependensinya.
- **Aset:** dipakai untuk membentuk hasil, bukan dijadikan instruksi tersembunyi.

Spesifikasi terbuka menyarankan isi SKILL.md kurang dari sekitar 5.000 token dan 500 baris, sedangkan artikel OpenAI terbaru menekankan deskripsi singkat dan pemuatan selektif. Angka itu **pedoman desain**, bukan alasan memangkas instruksi penting tanpa pemeriksaan. [S2][S11]

### 5.4 Dampak syarat “satu berkas” pada proyek ini

Dokumen **AI Skill Architect.md** yang sedang dibaca adalah **satu berkas kajian** yang memuat bahan penelitian lengkap. Menyalin seluruh kajian ini mentah-mentah ke SKILL.md akan membuat Skill berat dan mencampur uraian bagi manusia dengan instruksi bagi AI. Untuk tahap pemasangan kelak, usulan pertama ialah **satu berkas SKILL.md yang diringkas**; jika uji menunjukkan materi tertentu perlu dipisah, keputusan itu harus dikomunikasikan kepada pemilik Skill. Draf awal yang dapat ditinjau ada pada §13. Saat ini **tidak ada Skill terpasang dari berkas ini**.

---
