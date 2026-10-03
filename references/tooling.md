# Pemeriksaan dan operasi platform

## Ikuti host

Baca `skill-creator` yang berlaku ketika membuat, mengedit, atau memasang Skill.
Gunakan direktori personal yang ditentukan host. Jangan menyimpulkan bahwa
lokasi tidak bisa ditulis dari nama jalur saja. Pertahankan direktori dengan
identitas yang dikelola host; kesamaan folder dengan `name` berlaku untuk paket
portabel baru, bukan alasan mengganti identitas instalasi.

Gunakan validator host lebih dahulu. Simpan dan periksa status persisten sesuai
prosedur host. Jangan menyimpan salinan skill terpasang sebagai artefak baru
yang tidak diminta, dan jangan menyebut sukses sebelum verifikasi berhasil.

## Pemeriksa tambahan

`scripts/audit_skill.py` melakukan pemeriksaan statis baca-saja, tidak memasang
atau menjalankan isi Skill. Dependensi: Python 3.10+ dan PyYAML. Bila dependensi
tidak tersedia, laporkan pemeriksaan belum dijalankan; gunakan lingkungan yang
diizinkan atau validator host, jangan diam-diam mengubah dependensi global.

Jalankan dari direktori Skill Builder, memakai jalur target yang telah diresolve:

```bash
python3 scripts/audit_skill.py /path/to/skill
```

Tambahkan `--portable` **hanya** untuk paket yang memang harus mempunyai nama
folder sama dengan `name`. Mode default tidak menuntut pola nama direktori host.
Tambahkan `--json` untuk keluaran yang dapat dibaca mesin.

| Hasil | Makna |
| --- | --- |
| Exit 0 | Tidak ada kesalahan pada pemeriksaan yang diimplementasikan; warning mungkin ada |
| Exit 1 | Ada cacat statis yang harus ditinjau |
| Exit 2 | Pemeriksa tidak dapat berjalan atau argumen tidak sah |

Pemeriksa mencakup YAML tanpa kunci ganda, nilai `name`/`description`, isi utama,
berkas pendukung, tautan Markdown lokal sederhana di luar blok kode,
metadata tampilan bila ada, dan symlink. Referensi yang hilang atau keluar dari
folder ditandai; symlink tidak dibaca dan harus diganti/ditinjau sebelum hasil
dianggap lengkap. Placeholder adalah warning karena kadang merupakan contoh.

Pemeriksa tidak mengunjungi URL, memeriksa anchor Markdown, mengurai seluruh
varian CommonMark, membuktikan keamanan kode, memeriksa semua skema metadata
host, atau menguji mutu dan pemilihan otomatis Skill. Tinjau referensi berbentuk
backtick dan path dalam perintah secara manual. Warning membutuhkan penilaian,
bukan penghapusan otomatis. Field frontmatter tambahan diperingatkan untuk
diperiksa pada host; bukan otomatis dinyatakan melanggar spesifikasi terbuka.

Jika mengubah pemeriksa, jalankan [uji regresinya](../scripts/test_audit_skill.py):
`python3 scripts/test_audit_skill.py`. Fixture sementara dibuat di checkout
personal yang sama dan dibersihkan sesudah uji; tidak memasang Skill atau
mengakses layanan eksternal. Uji ini menguji kode pemeriksa, bukan perilaku AI.

## Metadata tampilan

Ikuti skema host saat mengubah `agents/openai.yaml`. Pastikan tampilan sesuai
fungsi, prompt awal memanggil nama Skill yang benar, dan aset yang ditunjuk
tersedia. Pertahankan kebijakan serta ikon yang sah dari instalasi sebelumnya.
Jangan menganggap metadata dependensi memberi akses atau izin baru.

## Ketika operasi gagal

- Kesalahan sintaks atau tautan: perbaiki sumber masalah, jalankan ulang bagian
  yang terkait. Jangan mengganti nama Skill untuk menghindari validator.
- Konflik versi: baca keadaan terbaru, gabungkan perubahan relevan, dan pakai
  prosedur pemulihan host. Jangan menimpa perubahan lain secara paksa.
- Akses ditolak: jelaskan tindakan yang belum selesai dengan bahasa sederhana;
  jangan mengaku berhasil atau mencoba melewati kontrol akses.
- UI belum menampilkan pembaruan: bedakan cache antarmuka dari status persisten.
  Jika host sudah terverifikasi, sarankan membuka ulang halaman Skills.
- Permintaan paket: periksa format yang didukung host saat itu. ZIP berisi
  folder Skill tidak otomatis berarti sudah terpasang, dan mengganti nama
  ekstensi tidak mengubah format isinya.
