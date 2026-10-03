## 9. Alat, skrip, integrasi, dan keamanan

### 9.1 Skill dan alat punya peran berbeda

Skill menjelaskan urutan kerja dan keputusan; alat atau server MCP menyediakan data langsung, autentikasi, pembacaan, dan tindakan. Skill tidak secara ajaib menciptakan akses yang tidak diberikan lingkungan. Jika tujuan memerlukan alat, sebut kapabilitas yang diperlukan, bukti keluaran, dan cabang jika alat gagal. [S4]

**Pola integrasi:**

~~~text
Permintaan → Pilih Skill → Periksa alat/izin → Ambil data seperlunya
→ Validasi hasil alat → Putuskan langkah → Susun keluaran → Verifikasi
~~~

Contoh: Skill membuat laporan rapat bisa membaca catatan yang tersedia, mengekstrak keputusan, dan membuat draf. Mengirim draf melalui layanan luar adalah langkah tersendiri yang mengikuti izin dan batas tindakan yang berlaku.

### 9.2 Kapan menulis skrip

Gunakan skrip ketika proses perlu determinisme atau berulang dengan input terdefinisi: mengurai berkas, memeriksa frontmatter, menghitung metrik, membentuk artefak, membandingkan skema. Jangan menambah skrip yang hanya memanggil model untuk menulis paragraf yang sama; kompleksitas baru harus dibayar oleh peningkatan keandalan. [S2][S4]

**Kontrak skrip yang baik:** nama dan tujuan; input dan validasi; output dan kode kegagalan; dependensi; contoh benar dan salah; pengujian kasus tepi; dampak samping yang mungkin terjadi.

### 9.3 Ancaman prompt injection

Sumber luar dapat mengandung teks “abaikan instruksi sebelumnya”, “unggah berkas rahasia”, atau “jalankan perintah ini”. Kalimat itu **isi sumber untuk diperiksa**, bukan otorisasi pengguna. Model Spec dan panduan keamanan OpenAI mendukung pemisahan instruksi tepercaya dari data tak tepercaya. Pengamanan perlu ada di beberapa lapisan karena instruksi tertulis saja tidak sempurna. [S7][S8]

| Ancaman | Gejala | Pengendalian dalam rancangan Skill |
| --- | --- | --- |
| Instruksi palsu di halaman/berkas | AI mengubah tugas setelah membaca sumber | Perlakukan teks eksternal sebagai data, cek tujuan asli |
| Pengeluaran data sensitif | Alat hendak mengirim isi berkas ke pihak lain | Batasi data, akses, dan tujuan; periksa aksi berdampak |
| Skrip tidak tepercaya | Kode pendukung mengakses lokasi/layanan tak relevan | Tinjau asal, dependensi, dan efeknya sebelum menjalankan |
| Izin berlebihan | Skill meminta akses ke semua layanan | Terapkan kebutuhan minimum untuk tugas saat ini |
| Klaim sumber palsu | Kutipan atau URL tidak mendukung fakta | Buka sumber, periksa klaim dan tanggal |
| Tindakan permanen | Penerbitan, penghapusan, atau pesan terkirim tak sengaja | Pastikan otorisasi pengguna dan batas lingkungan |

Dokumentasi OpenAI menegaskan Skill yang dijalankan bersama akses jaringan dan kode perlu ditinjau sebagai instruksi dan perangkat lunak yang berpengaruh pada tindakan. Dokumentasi keamanan plugin menganjurkan izin minimum, pemeriksaan masukan, dan konfirmasi pada operasi yang sulit dibalik. [S8][S15]

### 9.4 Privasi, lisensi, dan hak pemakaian

Jangan menyalin isi penuh materi berhak cipta ke Skill tanpa hak pemakaian; gunakan ringkasan yang sah dan tautan. Jangan masukkan kata sandi atau token ke SKILL.md. Untuk layanan pihak ketiga, tentukan data apa yang benar-benar diperlukan. Jika Skill dibagikan, tinjau lagi apakah referensi internal atau templat pribadi ikut terbawa. Persyaratan publikasi dan izin dapat berbeda menurut produk dan workspace; cek ulang sebelum distribusi. [S1][S15]

---

### 9.5 Tooling authoring bawaan

Tooling internal Skill Builder dibuat deterministik dan dapat diaudit.

- **Initializer** membuat struktur awal yang diminta tanpa menimpa direktori yang sudah ada.
- **Metadata builder** menghasilkan metadata antarmuka dari identitas Skill.
- **Validator** membaca dan menilai struktur serta metadata.
- **Auditor** memeriksa konsistensi berkas, referensi lokal, dan kondisi statis lain.

Setiap tool harus memberi kegagalan yang jelas ketika input tidak sah. Jalur authoring ini membuat Skill Builder tetap dapat membangun dan memeriksa Skill pada lingkungan yang tidak menyediakan creator bawaan.

