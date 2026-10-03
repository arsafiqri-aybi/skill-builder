## 2. Apa yang dimaksud dengan Skill

**Skill** adalah folder berisi alur kerja yang dapat dipakai ulang oleh ChatGPT/Codex. Paling sedikit ada sebuah berkas bernama **SKILL.md**, dengan metadata nama dan deskripsi serta isi instruksi. Skill dapat mengikutsertakan contoh, referensi, templat, dan skrip. Setelah tersedia, model dapat memilihnya ketika tugas cocok atau pengguna menyebutnya secara langsung. Skill berfungsi memberi **cara bekerja**, bukan melatih ulang bobot model dan bukan menjamin model selalu benar. [S1][S2][S3]

### Perbedaan wadah kerja

| Kebutuhan | Wadah yang biasanya tepat | Penalaran |
| --- | --- | --- |
| Satu permintaan yang jarang diulang | Prompt percakapan | Instruksi lokal untuk tugas saat ini cukup |
| Konteks dan berkas untuk satu proyek | Proyek dan instruksinya | Fokus pada pekerjaan dan materi yang berkaitan dalam proyek tersebut [S14] |
| Proses berulang dengan kondisi pemicu dan langkah yang jelas | Skill | Dapat dipakai kembali pada permintaan yang relevan [S1][S3] |
| Mengakses data langsung atau melakukan aksi di layanan lain | Alat/aplikasi atau server MCP | Menyediakan data, autentikasi, izin, serta tindakan nyata [S4] |
| Membagikan kumpulan Skill dan mungkin konektor | Plugin | Menjadi kemasan distribusi untuk kemampuan terkait [S3][S4] |
| Aplikasi yang mengontrol alur secara penuh | Implementasi API/agent | Memungkinkan kontrol eksplisit atas model, alat, skema, evaluasi, dan deployment [S13] |

**Aturan keputusan praktis:** jika isi yang dibutuhkan hanya “jawab sekali dengan gaya tertentu”, gunakan prompt. Jika pengetahuan atau proses itu berulang dan memiliki cara menentukan kapan dipakai, buat Skill. Jika perlu data langsung atau aksi eksternal, rancangkan alat yang sesuai; Skill dapat menjelaskan kapan dan bagaimana memakai alat itu. [S4]

### Penting bagi konteks pengguna ini

Sebagian host dapat menyediakan tooling native untuk membuat atau memvalidasi Skill. Skill Builder tidak bergantung pada tooling tersebut: desain, scaffolding, metadata, validasi, evaluasi, dan repair tersedia sebagai satu workflow internal. Tooling host diperlakukan sebagai pemeriksaan kompatibilitas tambahan bila tersedia. Tetap uji deskripsi dan trigger agar Skill Builder tidak terpilih untuk setiap percakapan mengenai AI. [S1][S3][S11]

---
