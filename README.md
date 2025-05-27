# VidozaCLI – Alat CLI Python Pengunduh Video Aman Tanpa Iklan

![VidozaCLI - Logo](https://github.com/user-attachments/assets/020cf2e7-5c77-45ed-b5d9-711038688ee6)

> **VidozaCLI** adalah alat baris perintah (_CLI tool_) modern untuk mengunduh video dari Videq dan platform serupa tanpa iklan berbahaya, malware, atau gangguan lainnya. Dirancang untuk pengalaman pengguna yang aman, cepat, dan bebas hambatan.

## 📚 Latar Belakang

Platform streaming seperti [`videq.com`](https://videq.com) sering kali menyajikan konten bermanfaat, namun iklan agresif dan potensi malware dapat mengganggu kenyamanan serta keamanan pengguna. **VidozaCLI** hadir sebagai solusi: mengunduh video langsung tanpa membuka peramban, tanpa iklan, dan tanpa risiko.

Dengan rekayasa permintaan HTTP tingkat lanjut, VidozaCLI meniru interaksi peramban yang sah, melewati mekanisme keamanan sederhana, dan memastikan pengunduhan yang bersih serta efisien.

## ✨ Fitur Utama

- **Pengunduhan Konkuren:** Menggunakan `asyncio` & `aiohttp` untuk unduhan paralel.
- **Lintas Platform:** Kompatibel dengan Linux, Windows, dan macOS.
- **Bebas Iklan & Malware:** Tidak perlu membuka browser, langsung unduh video .mp4.
- **Multi-Tautan:** Bisa unduh banyak video sekaligus dalam satu perintah.
- **Antarmuka Profesional:** Progress bar & logging berwarna untuk setiap unduhan.
- **Penamaan Berkas Otomatis:** Nama file otomatis dari judul video, sudah disanitasi.

## ⚡ Instalasi

> **Persyaratan:** Python 3.8 atau lebih baru.

1. **Kloning Repositori**
   
   ```bash
   git clone https://github.com/RozhakDev/VidozaCLI.git
   cd VidozaCLI
   ```

2. **Instal Dependensi**
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Instalasi Editable (Opsional)**
   
   ```bash
   pip install -e .
   ```

## 🚀 Penggunaan

Setelah instalasi, gunakan perintah `vidozaCLI` atau jalankan modul secara langsung.

### Sintaks Dasar

```bash
vidozaCLI <tautan_1> <tautan_2> ... [opsi]
```

### Contoh

- **Unduh satu video:**
  
  ```bash
  vidozaCLI https://videq.co/e/z40jeu954mk5
  ```
- **Unduh beberapa video sekaligus:**
  
  ```bash
  vidozaCLI https://videq.co/e/z40jeu954mk5,https://videq.my/d/z40jeu954mk5
  ```
- **Simpan ke direktori tertentu:**
  
  ```bash
  vidozaCLI https://videq.co/e/z40jeu954mk5 -o "D:/Koleksi Video/Anime"
  ```
- **Mode verbose untuk debugging:**
  
  ```bash
  vidozaCLI https://videq.co/e/z40jeu954mk5 -v
  ```

## 🗂️ Struktur Proyek

```text
VidozaCLI/
├── vidoza_downloader/
│   ├── main.py           # Titik masuk CLI & parser argumen
│   ├── downloader.py     # Logika inti pengunduhan
│   ├── network.py        # Pengelola sesi & header HTTP
│   ├── parser.py         # Parsing HTML & Regex
│   ├── logger.py         # Logging kustom
│   └── utils.py          # Utilitas (sanitasi nama file, dll)
├── tests/                # Unit tests
├── pyproject.toml        # Definisi proyek & dependensi
└── README.md             # Dokumentasi ini
```

## 🤝 Kontribusi

Kontribusi sangat terbuka! Ikuti langkah berikut:

1. **Fork** repositori ini.
2. Buat branch fitur (`git checkout -b fitur/NamaFitur`).
3. Commit perubahan (`git commit -m 'Menambahkan Fitur X'`).
4. Push ke branch Anda (`git push origin fitur/NamaFitur`).
5. Buka **Pull Request**.

Pastikan kode mengikuti standar gaya dan sertakan dokumentasi relevan.

## 📄 Lisensi

Proyek ini menggunakan **MIT License**. Lihat [LICENSE](LICENSE) untuk detail.