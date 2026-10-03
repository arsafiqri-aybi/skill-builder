# Merancang Skill dari pekerjaan nyata

## Kontrak sebelum instruksi

Rumuskan kontrak singkat; tidak perlu memaksakan tabel kepada pengguna.

| Komponen | Pertanyaan penentu |
| --- | --- |
| Pekerjaan | Hasil apa yang bisa dipakai setelah Skill selesai? |
| Pemicu | Permintaan apa yang memang membutuhkan prosedur ini? |
| Batas | Permintaan terdekat apa yang harus ditangani tanpa Skill ini? |
| Masukan | Apa yang wajib diketahui, dan apa yang dapat diasumsikan? |
| Sumber kebenaran | Dokumen, data, standar, atau layanan mana yang berwenang? |
| Keluaran | Apa bentuk, pembaca, dan kriteria penerimaan hasil? |
| Aksi | Apa yang dibaca, diubah, atau dikirim berdasarkan izin pengguna? |
| Kegagalan | Apa yang dilakukan saat input, sumber, atau alat tidak cukup? |

Jika tujuan sudah jelas, kerjakan. Tanyakan satu hal penentu bila dua pilihan
akan menghasilkan Skill yang berbeda secara mendasar. Jangan meminta pengguna
mendesain arsitektur, memilih nama folder internal, atau menyetujui perbaikan
rutin. Nyatakan asumsi hanya ketika berpengaruh pada hasil.

## Pilih ukuran dan bentuk

- Gunakan satu Skill untuk satu pekerjaan yang dapat dikenali, meski memiliki
  beberapa tahap. Pisahkan bila pemicu, izin, atau ukuran sukses berbeda.
- Gunakan referensi untuk pengetahuan yang dibaca selektif, bukan sebagai
  tempat menyembunyikan instruksi penting. Beri tautan dari `SKILL.md` dan
  kondisi kapan membukanya. Hindari rantai referensi yang dalam.
- Tambahkan skrip untuk pemeriksaan atau transformasi yang perlu konsisten.
  Tentukan input, output, dependensi, kegagalan, dan efek sampingnya.
- Pertahankan format tunggal jika pengguna memintanya. Jangan memasukkan seluruh
  kajian sebagai instruksi hanya karena kajiannya panjang.
- Hapus paragraf yang tidak memengaruhi keputusan atau keluaran. Pertahankan
  batas penting walaupun membuat isi sedikit lebih panjang.

## Deskripsi yang membedakan pekerjaan

Contoh rancangan lokal, bukan daftar kata pemicu resmi:

| Terlalu luas | Lebih tepat |
| --- | --- |
| Gunakan untuk AI, produktivitas, dan pekerjaan berkualitas | Buat atau perbaiki Skill dan SKILL.md dari kebutuhan pengguna |
| Gunakan saat membahas PDF | Ringkas temuan penelitian dari PDF yang diberikan pengguna |
| Selalu gunakan untuk database | Tulis dan tinjau migrasi skema beserta langkah pemulihannya |

Uji variasi bahasa dan maksud. Contoh: “buat laporan rapat” menjalankan domain;
“buat Skill pembuat laporan rapat” adalah pekerjaan Skill Builder. Penyebutan
kata “skill” dalam arti kemampuan manusia juga bukan pemicu otomatis.

## Instruksi operasional

Gunakan pola **kondisi → tindakan → bukti**, seperlunya:

- Jika sumber bertentangan, periksa tanggal dan cakupan; tunjukkan konflik yang
  belum terpecahkan, jangan menggabungkannya menjadi kepastian palsu.
- Jika masukan tidak cukup untuk menghitung, laporkan data yang hilang; jangan
  mengisi angka dengan tebakan.
- Setelah mengubah berkas, periksa aspek yang menentukan kegunaannya; jangan
  menyebut berhasil berdasarkan keberadaan berkas saja.
- Jika layanan gagal setelah aksi tulis, periksa status sebelum mencoba ulang
  agar tidak membuat duplikat. Untuk aksi baca, gunakan percobaan ulang terbatas.

Gunakan contoh hanya untuk keputusan atau format yang sulit dijelaskan.
Contoh bukan jawaban yang harus dihafal; jangan bocorkan jawaban eval ke isi.
Jangan mewajibkan gaya berpikir internal atau jumlah langkah untuk semua tugas.

## Memperbaiki Skill yang sudah ada

1. Ambil versi aktif, contoh kegagalan bila tersedia, serta preferensi yang
   harus dipertahankan. Bandingkan dengan hasil yang diminta sekarang.
2. Kelompokkan masalah: pemilihan Skill, instruksi, bahan, alat, atau pelaporan.
3. Ubah bagian penyebab. Deskripsi tidak akan memperbaiki algoritme salah;
   menambah referensi tidak akan memperbaiki tautan yang tidak pernah dibaca.
4. Pertahankan identitas pemasangan dan metadata host yang masih relevan.
   Jangan membuat Skill kedua hanya untuk menyimpan revisi.
5. Periksa kegagalan lama dan satu kasus tetangga yang mungkin terkena dampak.

“Lebih baik” berarti hasil memenuhi kriteria dengan lebih sedikit kegagalan
atau beban yang tidak perlu. Nama model, panjang berkas, dan banyaknya aturan
bukan ukuran mutu. Untuk klaim perbandingan model atau versi, perlukan uji
berpasangan dengan tugas, alat, dan kondisi sebanding.


## Membangun struktur Skill dari nol

Gunakan progressive disclosure agar context tetap hemat:

1. **Metadata** menjelaskan identitas dan kapan Skill dipilih.
2. **SKILL.md** menyimpan prosedur inti, keputusan penting, batas, dan syarat selesai.
3. **references/** menyimpan detail yang hanya dibuka pada kondisi tertentu.
4. **scripts/** menyimpan operasi deterministik atau pemeriksaan berulang.
5. **assets/** menyimpan bahan keluaran yang tidak perlu dibaca ke context.
6. **agents/** menyimpan metadata antarmuka host bila digunakan.

Pilih tingkat kekakuan berdasarkan risiko. Tugas fleksibel cukup memakai prinsip dan heuristik; tugas yang rapuh membutuhkan urutan, validasi, atau script yang lebih deterministik. Jangan membuat struktur hanya karena direktori tersedia.

Untuk Skill baru, mulai dari scaffold minimum, bukan dari template besar. Tambahkan hanya komponen yang punya fungsi nyata. Deskripsi harus memisahkan dengan jelas: kapan Skill ini dipakai, pekerjaan apa yang diselesaikan, dan permintaan mirip apa yang seharusnya tidak memicunya.

## Metadata dan scaffold

Gunakan `scripts/init_skill.py` untuk membuat paket baru ketika filesystem tersedia. Script tersebut membuat identitas dasar dan hanya direktori resource yang benar-benar diminta.

Gunakan `scripts/build_metadata.py` untuk menghasilkan atau memperbarui `agents/openai.yaml` dari identitas Skill. Metadata UI tidak boleh mengubah pekerjaan inti atau memberi kemampuan baru. Setelah scaffolding, isi runtime berdasarkan kontrak tugas dan hapus placeholder yang tersisa sebelum validasi.

## Acceptance floor untuk Skill baru

Sebelum dianggap selesai, pastikan:

- nama dan description valid serta membedakan pekerjaan,
- runtime berisi workflow yang dapat dijalankan,
- referensi dan scripts memiliki kondisi pemakaian yang jelas,
- tidak ada dependency tersembunyi yang tidak tersedia,
- local links dan metadata konsisten,
- ada contoh pemicu positif, negatif, dan failure case untuk perubahan besar,
- validasi statis lulus,
- klaim behavior atau installation hanya dibuat jika benar-benar diuji.
