# Pemeriksaan dan operasi platform

## Ikuti host tanpa dependency wajib

Gunakan aturan host yang benar-benar tersedia untuk lokasi, pemasangan,
persistensi, dan metadata. Skill Builder membawa tooling authoring sendiri untuk
scaffold, metadata, dan pemeriksaan statis; capability host tambahan dapat dipakai
bila membantu, tetapi bukan syarat agar desain Skill dapat berjalan.

Pertahankan direktori dengan identitas yang dikelola host. Kesamaan folder dengan
`name` hanya diwajibkan ketika membangun paket portabel yang memang memakai
aturan tersebut. Jangan mengganti identitas instalasi hanya demi menyamakan nama
folder.

Jika host punya validator atau installer native, gunakan sebagai pemeriksaan
tambahan dan verifikasi hasil persistennya. Jangan menyebut pemasangan berhasil
hanya karena paket lokal valid.

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


## Tool authoring bawaan Skill Builder

### Scaffold baru

```bash
python3 scripts/init_skill.py my-skill --path /target --description "Jelaskan pekerjaan dan kapan digunakan."
```

Tambahkan `--resources references,scripts,assets` hanya untuk resource yang memang dibutuhkan. Script tidak menimpa direktori yang sudah ada.

### Metadata host

```bash
python3 scripts/build_metadata.py /path/to/my-skill
```

Nilai tampilan dapat dioverride dengan opsi CLI. Metadata yang dihasilkan harus tetap selaras dengan `SKILL.md`.

### Validasi

```bash
python3 scripts/validate_skill.py /path/to/my-skill --portable
```

Validator terpadu memanggil pemeriksaan statis Skill Builder dan menghasilkan exit code yang bisa dipakai CI. Ini tidak membuktikan kualitas perilaku, keamanan menyeluruh, atau keberhasilan instalasi.
