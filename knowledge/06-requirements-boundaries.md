## 6. Merumuskan kebutuhan dan batas Skill

### 6.1 Mulai dari permintaan nyata

Jangan mulai dengan daftar perintah panjang. Kumpulkan beberapa contoh kalimat pengguna:

- “Buat Skill untuk membuat modul belajar dari jurnal resmi.”
- “Perbaiki Skill ini karena terlalu sering aktif ketika aku hanya bertanya tentang topiknya.”
- “Audit Skill yang membuat laporan; hasilnya tidak menyertakan sumber.”
- “Aku hanya ingin penjelasan apa itu Skill.” → ini **belum tentu** permintaan membuat atau mengaudit Skill.

Untuk setiap contoh, catat: **masukan yang tersedia, tindakan yang dapat diambil, berkas yang diperlukan, hasil akhir, kriteria benar, dan cara menangani informasi yang hilang**.

### 6.2 Kontrak Skill

| Komponen | Pertanyaan yang harus dijawab | Contoh Skill riset pembelajaran |
| --- | --- | --- |
| Tujuan | Pekerjaan apa yang selesai? | Modul belajar berbasis sumber |
| Pemakai | Siapa yang memakai hasil? | Pembelajar pemula |
| Pemicu | Apa ungkapan yang cocok? | “Buat modul belajar dengan rujukan” |
| Bukan pemicu | Ungkapan tetangga yang tidak cocok? | “Apa arti istilah ini?” |
| Input wajib | Apa yang tidak bisa ditebak? | Topik modul |
| Input opsional | Apa yang bisa diasumsikan wajar? | Durasi belajar, tingkat bahasa |
| Sumber fakta | Dari mana data diambil? | Artikel dan dokumentasi primer |
| Alur inti | Langkah mana yang perlu? | Tentukan cakupan → cari sumber → susun → periksa |
| Bentuk output | Apa yang diserahkan? | Modul, latihan, sitasi |
| Selesai | Bagaimana tahu tugas rampung? | Setiap klaim penting didukung dan materi dapat dipakai |
| Izin | Tindakan mana yang mengubah akun/layanan? | Unggah/publikasi memerlukan otorisasi sesuai konteks |

### 6.3 Memilih ukuran Skill

Satu Skill sebaiknya mempunyai **tujuan pengguna yang dapat dikenali**. Jika dua alur punya pemicu, masukan, atau ukuran sukses yang berbeda, pertimbangkan dua Skill. Sebaliknya jangan memecah alur yang sama menjadi puluhan Skill kecil tanpa manfaat pemilihan; terlalu banyak deskripsi bisa saling tumpang tindih dan memakan konteks. [S4][S11]

**Contoh:** “membuat modul dari sumber” dan “menerjemahkan modul yang sudah jadi” cenderung berbeda. Tetapi “membuat modul 5 bab” dan “membuat modul 7 bab” biasanya variasi input dari Skill yang sama.

### 6.4 Tingkat kebebasan instruksi

| Situasi | Instruksi yang cocok |
| --- | --- |
| Tugas kreatif atau konteks bervariasi | Prinsip, contoh, dan kriteria hasil; beri ruang keputusan |
| Format stabil tetapi isi berubah | Templat dengan parameter dan titik keputusan |
| Operasi rapuh atau harus identik | Skrip dengan validasi masukan/keluaran |

Rancangan Skill Builder menggunakan kebebasan tinggi untuk menjelajahi kebutuhan, menengah untuk menyusun berkas, dan rendah untuk validasi struktur. Ini rekomendasi arsitektur, bukan aturan platform.

---
