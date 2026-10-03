## 8. Pengetahuan domain, referensi, dan sumber

### 8.1 Pengetahuan Skill perlu dibagi menurut peran

| Lapisan | Isi | Tempat yang cocok |
| --- | --- | --- |
| Pengetahuan prosedural | Apa yang dilakukan dalam urutan apa | SKILL.md |
| Pengetahuan deklaratif | Standar, daftar istilah, skema, kebijakan | references/ jika panjang |
| Pengetahuan contoh | Permintaan pengguna, contoh hasil, anti-contoh | SKILL.md jika sedikit; referensi jika banyak |
| Pengetahuan alat | Nama, masukan, keluaran, batas, kegagalan | SKILL.md atau referensi integrasi |
| Pengetahuan pemilik | Gaya, prioritas, ambang kualitas | Masukkan hanya yang memang stabil dan relevan |

**Pemisahan penting:** menambahkan 50 halaman domain ke Skill tidak sama dengan merancang cara menggunakan bahan tersebut. AI perlu petunjuk kapan membaca, bagian mana relevan, cara mengecek versi, dan cara mengatasi sumber yang bertentangan.

### 8.2 Tata kelola fakta

Untuk topik yang berubah, simpan dalam referensi: **tautan sumber primer, tanggal diperiksa, wilayah/versi yang berlaku, klaim yang didukung, dan pemicu untuk memeriksa ulang**. Jangan menyimpan harga, jadwal, aturan hukum, atau daftar model sebagai fakta abadi. Jika sumber resmi dan sumber sekunder berbeda, verifikasi konteks dan tanggal, lalu jelaskan konflik yang tersisa.

**Contoh entri acuan:**

~~~text
Topik: format SKILL.md
Sumber: Agent Skills Specification [S2]
Diperiksa: 2026-09-24
Memakai untuk: nama, description, frontmatter, folder
Periksa ulang ketika: akan memasang Skill baru atau validator mengeluh
~~~

### 8.3 Klaim dan bukti

Setiap klaim yang menentukan tindakan harus bisa ditelusuri. Kelompokkan:

- **Klaim format:** lihat spesifikasi.
- **Klaim produk:** lihat panduan ChatGPT/Codex saat eksekusi.
- **Klaim teknis:** lihat dokumentasi pembuat alat.
- **Klaim dampak:** bila dinyatakan empiris, lihat studi dengan metode dan batas jelas.
- **Preferensi pemilik:** tanyakan bila tidak dapat ditarik dari instruksi yang ada.

OpenAI menjelaskan bahwa penyediaan konteks relevan dan pengujian prompt membantu kualitas; OpenAI juga mengingatkan keluaran bisa salah. Karena itu, referensi menyediakan **bahan untuk diverifikasi**, bukan hak untuk mengarang isi yang tidak dapat ditemukan. [S9][S13]

### 8.4 Kapan referensi perlu tetap satu berkas

Untuk Skill sangat ringkas, satu SKILL.md sering cukup. Bila hanya dokumentasi penelitian yang harus berada dalam satu berkas, tetap mungkin menyimpan riset sebagai berkas tunggal terpisah dari Skill operasional. Penggabungan semua referensi ke SKILL.md hanya masuk akal bila bagian itu benar-benar dibutuhkan hampir setiap pemakaian dan hasil uji tidak menurun. [S2][S11]

---
