## 11. Kegagalan umum dan diagnosis

| Gejala | Penyebab yang mungkin | Perbaikan yang paling tepat |
| --- | --- | --- |
| Skill tidak terpilih | Deskripsi samar, kata inti terlambat, lingkungan tidak memuat Skill | Sempitkan dan majukan pemicu; cek ketersediaan |
| Skill aktif pada hampir semua tugas | Deskripsi memakai kata umum seperti “AI”, “data”, “dokumen” | Sebut tujuan pengguna yang spesifik; tambah kasus negatif |
| Isi SKILL.md tidak dipakai | Skill tidak pernah terpilih atau instruksi tersimpan hanya dalam referensi tak ditautkan | Uji pemicu, jelaskan kapan membuka referensi |
| Jawaban terdengar pasti tetapi salah | Tidak ada sumber, versi usang, model menebak | Tautkan sumber, wajibkan verifikasi saat diperlukan |
| AI menanyakan terlalu banyak hal | Terlalu banyak prasyarat sepele | Bedakan wajib dan opsional; buat asumsi yang wajar |
| AI berhenti di rencana | Definisi selesai tidak termasuk implementasi dan verifikasi | Tentukan keluaran akhir dan langkah pemeriksaan |
| AI melakukan terlalu banyak langkah | Instruksi mewajibkan riset/tes penuh pada semua kasus | Buat cabang berdasarkan risiko dan kebutuhan |
| Skill rusak setelah pembaruan | Referensi atau skrip usang; uji tidak dijalankan | Catat perubahan dan uji regresi terarah |
| Berkas valid tetapi hasil buruk | Validator hanya menguji bentuk | Tambahkan uji tugas nyata dan rubrik manusia |
| Kode pendukung berbahaya/keliru | Tidak ditinjau atau belum diuji | Audit dependensi, izin, dan jalankan kasus representatif |
| Skill bertabrakan dengan Skill lain | Dua deskripsi terlalu mirip | Tegaskan batas berdasarkan pekerjaan, bukan kata umum |
| Prompt injection dari sumber | AI menganggap teks web sebagai perintah | Pisahkan data dari instruksi; cek alat dan izin |

**Prinsip diagnosis:** gunakan artefak yang gagal, bukan dugaan semata. Ubah satu bagian yang terkait dengan kegagalan, lalu ulangi kasus yang gagal dan kasus tetangganya. [S5][S8]

---
