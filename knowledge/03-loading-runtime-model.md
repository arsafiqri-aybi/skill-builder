## 3. Model mental: bagaimana Skill bekerja

### 3.1 Tiga tahap pemuatan

1. **Penemuan:** lingkungan memperlihatkan setidaknya nama dan deskripsi Skill yang tersedia.
2. **Pemilihan:** model memilih berdasarkan kecocokan permintaan atau pengguna memanggil Skill secara eksplisit.
3. **Penggunaan:** isi SKILL.md dibaca; berkas pendukung dimuat atau skrip dijalankan hanya ketika diperlukan dan tersedia.

Inilah alasan kalimat pada **deskripsi** lebih berpengaruh terhadap pemilihan daripada paragraf “kapan digunakan” yang tersembunyi di badan SKILL.md. Dokumentasi OpenAI menyebut pemanggilan eksplisit di ChatGPT dengan memilih Skill melalui **@**; di Codex dapat menggunakan **$** atau daftar Skill. Pemanggilan implisit mengikuti deskripsi. [S2][S3]

### 3.2 Skill adalah instruksi kerja, bukan sumber kebenaran otomatis

Model bahasa menghasilkan keluaran yang dapat bervariasi dan kadang keliru. Penelitian OpenAI membahas mengapa model dapat menebak alih-alih menyatakan ketidakpastian. Karena itu Skill yang memerlukan fakta terkini harus menjelaskan **kapan memeriksa sumber, bagaimana melaporkan ketidakpastian, dan bagaimana menghubungkan klaim dengan bukti**. Instruksi “selalu benar” tidak menyediakan mekanisme tersebut. [S9][S12]

### 3.3 Instruksi memiliki tingkat otoritas

Model memiliki aturan prioritas instruksi. Berkas Skill tidak dapat mengambil alih aturan tingkat lebih tinggi atau izin pengguna, dan tulisan yang muncul di halaman web, lampiran, hasil pencarian, dan keluaran alat tidak otomatis menjadi perintah. Penelitian tentang hierarki instruksi dan panduan keamanan OpenAI menjelaskan mengapa mengangkat teks tak tepercaya menjadi perintah menimbulkan risiko prompt injection. [S7][S8]

**Konsekuensi desain:** tulis peraturan yang mengarahkan AI menghormati instruksi yang berlaku, memisahkan **data untuk dianalisis** dari **perintah untuk dilaksanakan**, dan meminta izin bila tugas yang bersangkutan memang mensyaratkannya. Jangan menulis “abaikan seluruh instruksi lain” atau klaim prioritas palsu.

### 3.4 Konteks terbatas dan relevansi menentukan

Seluruh instruksi, riwayat, dokumen, dan hasil alat bersaing untuk ruang konteks. Spesifikasi Agent Skills merekomendasikan metadata pendek, isi utama SKILL.md ringkas, dan referensi panjang hanya saat diperlukan. Penelitian “Lost in the Middle” menemukan bahwa pada model dan tugas yang diuji, informasi relevan dalam konteks panjang tidak selalu digunakan sama baiknya di semua posisi. **Ini mendukung strategi pemuatan selektif**, bukan bukti bahwa semua model terbaru selalu gagal ketika dokumen panjang. [S2][S10][S11]

### 3.5 Variasi harus dihadapi dengan evaluasi

Satu contoh keberhasilan belum membuktikan Skill andal. Evaluasi harus mencakup tugas nyata, contoh yang harus memicu Skill, contoh yang tidak boleh memicu, ragam ungkapan, kegagalan alat, dan perubahan model atau dokumen. Kualitas hasil, kepatuhan pada proses, gaya, dan efisiensi dapat dinilai terpisah. [S5][S6]

---
