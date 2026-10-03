## 7. Menulis instruksi yang kuat

### 7.1 Deskripsi adalah penentu pemilihan

**Lemah:** “Membantu semua kebutuhan AI, riset, desain, dan pembuatan Skill.”  
**Lebih tepat:** “Rancang atau audit Skill ChatGPT dari contoh kebutuhan pengguna; buat kontrak masukan/keluaran, instruksi SKILL.md, dan kasus uji pemicu. Gunakan saat pengguna meminta membuat atau memperbaiki Skill.”

Kalimat pertama terlalu luas dan bisa memicu Skill pada hampir semua pertanyaan AI. Kalimat kedua menyebut **pekerjaan**, **hasil**, dan **kondisi pemicu**. Dokumentasi OpenAI menganjurkan deskripsi ringkas, kata pemicu di depan, dan lingkup jelas; ketika ada banyak Skill, deskripsi yang panjang dapat dipotong oleh lingkungan. [S3][S11]

### 7.2 Tuliskan alur sebagai keputusan yang dapat diamati

Bandingkan:

- Kabur: “Pahami semua kebutuhan, gunakan cara terbaik, hasil harus sempurna.”
- Dapat dijalankan: “Catat 3 contoh permintaan yang harus memakai Skill dan 2 contoh serupa yang tidak. Jika tujuan belum cukup jelas untuk menentukan output, ajukan satu pertanyaan inti. Tulis SKILL.md; periksa frontmatter dan nama folder; uji contoh positif dan negatif; laporkan yang belum diuji.”

Instruksi yang baik menyatakan **pemicu, tindakan, sumber, syarat, output, dan penanganan gagal**. Gunakan kata kerja yang konkret. Jangan mengulang pengetahuan umum yang sudah dimiliki model kecuali perlu untuk keputusan tertentu. [S3][S4]

### 7.3 Contoh harus membantu, bukan mengunci

Mulailah dengan instruksi sederhana. Tambahkan contoh masukan/keluaran ketika format atau keputusan sulit disampaikan dengan kalimat pendek; pastikan contoh tidak bertentangan dengan aturan. Panduan model penalaran OpenAI memperingatkan bahwa perintah “pikir langkah demi langkah” tidak selalu meningkatkan kinerja; tujuan dan batas yang jelas lebih berguna. [S13]

### 7.4 Hindari janji yang tidak dapat ditepati

Kalimat “selalu cari internet” gagal bila alat tidak tersedia; “selalu simpan otomatis” gagal bila akses berkas tidak ada; “jamin tidak berhalusinasi” tidak operasional. Tulis kondisi:

- “Jika informasi bergantung pada kondisi terbaru dan pencarian tersedia, periksa sumber resmi.”
- “Jika sumber tidak dapat diakses, nyatakan keterbatasan dan jangan mengarang kutipan.”
- “Sebelum menyatakan selesai, pastikan keluaran sesuai kriteria yang ditulis.”

### 7.5 Selaraskan dengan instruksi pengguna dan izin

Skill memberikan metode kerja; ia tidak boleh mengklaim prioritas di atas instruksi tingkat lebih tinggi, mengabaikan perubahan permintaan pengguna yang sah, atau meminta akses berlebih. Penulis Skill perlu menentukan **kapan klarifikasi diperlukan**, **kapan asumsi aman**, dan **kapan tindakan berisiko memerlukan otorisasi** sesuai lingkungan. [S7][S8]

### 7.6 Membuat instruksi dapat diaudit

Tautkan setiap aturan penting ke salah satu dari:

1. **Kriteria hasil:** “sertakan rujukan primer untuk klaim teknis yang bergantung versi.”
2. **Kriteria proses:** “validasi berkas setelah menulisnya.”
3. **Kriteria batas:** “jangan menerbitkan atau memasang ketika pengguna baru meminta draf.”
4. **Kriteria kegagalan:** “jelaskan apa yang tidak bisa diverifikasi.”

Jika satu aturan tidak memengaruhi keputusan, hasil, atau keselamatan, pertimbangkan menghapusnya.

---
