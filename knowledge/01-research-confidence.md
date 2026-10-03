## 1. Metode riset dan tingkat kepastian

Kajian ini mengutamakan tiga kelas sumber: **dokumentasi produk OpenAI** untuk perilaku ChatGPT/Codex yang berlaku saat ini; **spesifikasi Agent Skills** untuk format berkas; serta **panduan teknis dan riset asli** untuk alasan di balik pengujian, batas konteks, hierarki instruksi, dan keamanan. Semua tautan utama ada di §15.

| Jenis pernyataan | Cara memperlakukannya | Contoh |
| --- | --- | --- |
| Aturan format | Ikuti spesifikasi dan batas lingkungan tempat Skill dipasang; periksa kembali sebelum memasang | YAML frontmatter, nama direktori, berkas SKILL.md [S2] |
| Perilaku produk | Periksa panduan produk terbaru karena antarmuka dan kelayakan berubah | Pemanggilan eksplisit/otomatis dan ketersediaan ChatGPT [S1][S3] |
| Temuan penelitian | Berlaku untuk lingkungan yang diuji dalam penelitian, bukan jaminan semua model | Sensitivitas terhadap posisi informasi dalam konteks panjang [S10] |
| Rekomendasi rekayasa | Gunakan sebagai hipotesis yang perlu dievaluasi pada kasus pengguna | Ambang keberhasilan pengujian yang diajukan pada §10 |
| Contoh rancangan | Ilustrasi untuk disesuaikan, bukan kemampuan platform yang dijamin | Draf AI Skill Architect pada §13 |

**Batas kajian:** sumber resmi dapat berubah; penelitian empiris tidak menjamin hasil pada semua model; contoh ambang pengujian di sini adalah **usulan rancangan**, bukan angka resmi OpenAI. Tidak ada pengujian langsung atas AI Skill Architect terpasang pada tahap ini. Pemisahan itu penting supaya dokumen tidak mengklaim sesuatu yang belum diuji.

### Pertanyaan riset yang dijawab

1. Apa perbedaan Skill dengan prompt biasa, instruksi proyek, konektor, dan plugin?
2. Bagaimana model menemukan dan memuat Skill?
3. Pengetahuan apa saja yang dibutuhkan untuk merancang Skill?
4. Bagaimana menuliskan instruksi yang efektif tanpa membebani konteks?
5. Bagaimana menyusun bahan referensi, skrip, dan alat?
6. Bagaimana menguji pemicu, proses, keluaran, keamanan, dan ketahanan?
7. Bagaimana merancang AI Skill Architect sebagai Skill yang membangun Skill lain?

---
