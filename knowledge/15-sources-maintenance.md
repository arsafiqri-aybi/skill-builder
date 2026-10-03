## 15. Sumber primer dan catatan pemutakhiran

**Diperiksa pada 24 September 2026.** Tautan berikut mengarah ke sumber asli; ringkasan dalam dokumen ini adalah parafrasa yang dipakai untuk desain proyek. Untuk pekerjaan pemasangan, periksa ulang terutama [S1]–[S4] dan panduan instalasi lingkungan tujuan karena ketersediaan fitur dapat berubah.

| Kode | Sumber | Peran dan batas |
| --- | --- | --- |
| [S1] | [OpenAI Help Center, “Skills in ChatGPT”](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | Definisi, kelayakan, pembuatan, instalasi, pembagian, pemindaian; dapat berubah menurut produk/workspace |
| [S2] | [Agent Skills, “Specification”](https://agentskills.io/specification) | Format terbuka, field, struktur, pemuatan bertahap, validasi; sebagian field opsional tidak universal |
| [S3] | [OpenAI, “Build skills”](https://learn.chatgpt.com/docs/build-skills) | Cara ChatGPT/Codex memuat dan menggunakan Skill, metadata, praktik penulisan, opsi distribusi |
| [S4] | [OpenAI Developers, “Build skills”](https://developers.openai.com/plugins/build/skills) dan [“Skills: concepts”](https://developers.openai.com/plugins/concepts/skills) | Batas Skill dan MCP, alur, sumber pendukung, paket plugin |
| [S5] | [OpenAI Developers, “Testing Agent Skills Systematically with Evals”](https://developers.openai.com/blog/eval-skills) | Contoh uji pemicu, hasil, proses, gaya, dan efisiensi; contoh teknik bukan ambang wajib |
| [S6] | [OpenAI API, “Evaluation best practices”](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Tujuan evaluasi, dataset, metrik, penilaian manusia, kasus tepi; antarmuka produk evaluasi dapat berubah |
| [S7] | [OpenAI, “The Instruction Hierarchy”](https://openai.com/index/the-instruction-hierarchy/) dan [Model Spec](https://model-spec.openai.com/2025-04-11.html) | Prioritas instruksi dan perlakuan teks tak tepercaya; model spec versi tertaut berpenanggalan |
| [S8] | [OpenAI API, “Safety in building agents”](https://developers.openai.com/api/docs/guides/agent-builder-safety) dan [OpenAI API, “Skills: risks and safety”](https://developers.openai.com/api/docs/guides/tools-skills) | Prompt injection, izin alat, validasi, pemeriksaan Skill; contoh Agent Builder berada dalam transisi produk |
| [S9] | [OpenAI, “Why language models hallucinate”](https://openai.com/index/why-language-models-hallucinate/) | Penelitian asli tentang menebak dan ketidakpastian; bukan ukuran akurasi Skill Builder |
| [S10] | [Liu dkk., “Lost in the Middle: How Language Models Use Long Contexts”, TACL 2024](https://aclanthology.org/2024.tacl-1.9/) | Temuan empiris pada model dan tugas yang diuji; tidak digeneralisasikan sebagai kepastian semua model |
| [S11] | [OpenAI Developers, “Rethinking skills and prompts for GPT-6 Astra”](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Deskripsi ringkas, pemuatan selektif, dan risiko instruksi terlalu panjang |
| [S12] | [OpenAI Help Center, “Does ChatGPT tell the truth?”](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth) | Keterbatasan akurasi dan perlunya memeriksa informasi penting |
| [S13] | [OpenAI API, “Prompt engineering”](https://developers.openai.com/api/docs/guides/prompt-engineering) dan [“Reasoning best practices”](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | Instruksi, konteks, contoh, variasi model; bagian khusus API tidak otomatis sama dengan antarmuka ChatGPT |
| [S14] | [OpenAI Help Center, “Projects in ChatGPT”](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) | Peran proyek sebagai wadah chat, berkas, dan instruksi terkait |
| [S15] | [OpenAI Developers, “Security & Privacy” untuk plugin](https://developers.openai.com/plugins/guides/security-privacy) | Izin minimum, data sensitif, aksi tulis, pemeriksaan masukan, dan keamanan alat |

### Hal yang wajib diperiksa ulang sebelum tahap pemasangan

1. Apakah jenis akun dan antarmuka pengguna mendukung Skill yang dimaksud. Dokumentasi ChatGPT saat kajian ini menyebut kelayakan menurut paket, produk, dan pengaturan workspace; ketersediaan **tidak boleh ditebak** hanya dari adanya berkas Markdown. [S1]
2. Apakah spesifikasi metadata, jalur pemasangan, validator, dan cara pemanggilan masih berlaku. [S2][S3]
3. Apakah draf satu berkas pada §13 perlu menyesuaikan skill-creator bawaan dan Skill lain yang sudah ada. [S1][S11]
4. Apakah pengguna mengizinkan pembuatan/pemasangan setelah meninjau kajian ini. Sampai ada instruksi tersebut, statusnya tetap **dokumen penelitian**.

---

**Akhir berkas.** Keputusan tahap berikutnya yang perlu dipilih pemilik: apakah draf pada §13 akan diwujudkan sebagai Skill pribadi bernama **Skill Builder**, divalidasi, diuji, dan dipasang di ChatGPT.
