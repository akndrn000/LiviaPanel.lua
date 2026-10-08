<div align="center">

<img src="assets/banner.png" alt="Livia Panel: panel mobile untuk Roblox executor" width="100%">

<br>

![Lua](https://img.shields.io/badge/Lua-2C2D72?style=flat-square&logo=lua&logoColor=white)
![Roblox](https://img.shields.io/badge/Roblox_executor-000000?style=flat-square&logo=roblox&logoColor=white)
![Mobile](https://img.shields.io/badge/Mobile-friendly-7c5cff?style=flat-square)
![MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

[Bahasa Indonesia](README.md) · [English](README.en.md)

**Panel sederhana untuk Roblox executor, dibuat untuk layar HP.**
Lima fitur dalam satu panel. Satu file Lua, tanpa dependensi.

[Coba sekarang](#coba-sekarang) ·
[Fitur](#fitur) ·
[Cara pakai](#cara-pakai) ·
[Kontrol](#kontrol) ·
[Kustomisasi](#kustomisasi) ·
[Privasi](#privasi-dan-keamanan) ·
[Batasan](#batasan-yang-diketahui) ·
[Kontribusi](#kontribusi)

</div>

---

## Ringkasan

Executor di HP biasanya hanya memberi kotak teks, dan tombol kecil yang gampang tertekan saat layar digeser. Livia Panel menyatukan Speed, Jump, Fly, Ghost, dan ESP Player dalam satu panel dengan tombol ON/OFF dan kotak angka, lalu menjalankannya dari satu berkas Lua.

Ada tiga hal yang menjadi pegangan panel ini:

- **Satu file, satu panel.** Salin satu berkas ke executor, tekan Execute. Tanpa dependensi, tanpa pengaturan tambahan.
- **Aman disentuh.** Tombol hanya aktif saat ditekan singkat. Geseran lebih dari 10 px dianggap memindahkan panel, jadi menggeser tidak ikut menyalakan atau mematikan fitur.
- **Bersih saat ditutup.** Tombol `X` mematikan semua fitur, memutus semua koneksi, dan menghapus panel. Menjalankan script lagi tidak membuat panel dobel.

## Coba sekarang

Tiga langkah dari nol sampai panel tampil:

1. **Salin** isi [`LiviaPanel.lua`](LiviaPanel.lua) ke executor Anda (contoh: Delta).
2. Tekan **Execute**. Panel **LIVIA PANEL** muncul di layar.
3. Isi angka di kotak, lalu tekan **ON** pada fitur yang Anda mau.

> [!WARNING]
> Menggunakan script di game bisa melanggar Terms of Use Roblox dan berisiko membuat akun terkena sanksi. Baca [Batasan yang diketahui](#batasan-yang-diketahui) sebelum memakainya.

## Tampilan

<p align="center">
  <img src="assets/preview.png" alt="Tampilan panel Livia" width="360">
</p>

<p align="center"><sub>Ukuran panel 300×342, tinggi tiap baris 46, teks ukuran 14, jadi nyaman disentuh di HP. Nilai pada gambar adalah nilai contoh.</sub></p>

## Fitur

| | |
|---|---|
| **Speed** | Kecepatan lari. Angka + ON/OFF. Bawaan 50, kembali ke 16 saat OFF. |
| **Jump** | Tinggi lompat. Angka + ON/OFF. Bawaan 100, kembali ke 50 saat OFF. |
| **Fly** | Terbang. Angka adalah kecepatan terbang (bawaan 60). Karakter melayang bila joystick dilepas. |
| **Ghost** | Tembus tembok (noclip). ON/OFF. |
| **ESP Player** | Pemain lain terlihat tembus pandang lewat Highlight merah dengan garis tepi putih. ON/OFF. |
| **Tap, bukan geser** | Tombol hanya aktif saat ditekan singkat. Geseran lebih dari 10 px memindahkan panel. |
| **Geser dari mana saja** | Panel bisa digeser dari header, latar, baris, atau langsung dari tombol. |
| **Nilai langsung berlaku** | Angka di kotak bisa diubah saat fitur sedang ON dan langsung dipakai. |
| **Minimize** | Tombol `-` mengecilkan panel menjadi bulatan **L** yang bisa digeser. |
| **Tutup bersih** | Tombol `X` mematikan semua fitur dan menghapus panel. Menjalankan script lagi tidak membuat panel dobel. |

## Cara pakai

1. **Buka** game Roblox dan jalankan executor Anda (contoh: Delta).
2. **Salin** isi [`LiviaPanel.lua`](LiviaPanel.lua) ke executor lalu tekan **Execute**, atau pakai loadstring:

   ```lua
   loadstring(game:HttpGet("https://raw.githubusercontent.com/USERNAME/REPO/main/LiviaPanel.lua"))()
   ```

   Ganti `USERNAME` dan `REPO` dengan akun dan nama repository Anda.
3. **Isi angka** di kotak Speed, Jump, atau Fly bila ingin mengubah nilai awal.
4. **Tekan ON** pada fitur yang diinginkan. Tekan OFF untuk mematikannya.
5. Untuk **Fly**, gerakkan joystick untuk maju. Saat bergerak, arahkan kamera ke atas atau ke bawah untuk naik atau turun.
6. Tekan `-` untuk menyembunyikan panel, atau `X` untuk menutupnya sepenuhnya.

> [!TIP]
> Bila speed atau jump terasa ditarik balik oleh game, turunkan angkanya. Nilai yang lebih kecil lebih jarang memicu anti-cheat.

> [!NOTE]
> Panel dipasang di `CoreGui`, jadi executor Anda harus mengizinkan akses ke sana.

## Kontrol

| Tombol | Fungsi |
|---|---|
| `ON` / `OFF` | Menyalakan atau mematikan fitur pada baris itu. |
| Kotak angka | Mengatur nilai (Speed, Jump, Fly). Input yang bukan angka, atau angka negatif, dikembalikan ke nilai sebelumnya. |
| `-` | Menyembunyikan panel menjadi bulatan **L**. |
| **L** (bulat) | Membuka panel kembali. |
| `X` | Mematikan semua fitur lalu menutup panel. |
| Geser | Memindahkan panel. Geseran lebih dari 10 px dianggap menggeser, bukan menekan. |

### Nilai bawaan

| Fitur | Nilai awal | Saat dimatikan |
|---|---|---|
| Speed | 50 | `WalkSpeed` kembali ke 16 |
| Jump | 100 | `JumpPower` kembali ke 50 |
| Fly | 60 | Terbang berhenti dan karakter bisa berjalan lagi |
| Ghost | - | Tabrakan karakter diaktifkan kembali |
| ESP Player | - | Semua Highlight dihapus |

## Kustomisasi

Semua pengaturan ada di bagian atas `LiviaPanel.lua`.

| Yang ingin diubah | Cara |
|---|---|
| **Nilai awal** | Ubah tabel `V`, misalnya `local V = {Speed = 50, Jump = 100, Fly = 60}`. |
| **Warna** | Ubah tabel `T` (`Accent`, `On`, `Off`, `Red`, dan seterusnya). |
| **Sensitivitas geser** | Ubah `DRAG_THRESHOLD` (bawaan 10 px). Makin besar, makin sulit tombol tertekan tanpa sengaja saat sentuhan sedikit bergeser. |
| **Ukuran panel** | Ubah `Main.Size` dan tinggi baris di `createRow`. |

## Privasi dan keamanan

- Script **berjalan di sisi client** dan tidak mengirim data ke mana pun. Tidak ada panggilan jaringan di dalam `LiviaPanel.lua`.
- Tidak ada analytics, pelacak, atau penyimpanan data. Nilai kembali ke bawaan setiap kali script dijalankan ulang.
- Jangan menjalankan script dari sumber yang tidak Anda percaya. Jalankan hanya salinan yang Anda baca sendiri, atau dari repository Anda.

## Batasan yang diketahui

- **Anti-cheat.** Beberapa game punya anti-cheat. Jika speed atau jump terasa ditarik balik, gunakan angka yang lebih kecil.
- **Risiko akun.** Menggunakan script di game bisa melanggar Terms of Use Roblox dan berisiko membuat akun terkena sanksi. Gunakan dengan risiko sendiri.
- **Nilai pemulihan tetap.** Saat OFF, Speed selalu kembali ke 16 dan Jump ke 50, bukan ke nilai bawaan game bila game itu memakai nilai lain.
- **Fly bergantung pada kamera.** Naik dan turun hanya terjadi saat joystick digerakkan. Bergerak mundur membalik arah naik dan turun.
- **Tidak ada penyimpanan.** Nilai tidak diingat setelah script dijalankan ulang.
- **Bergantung pada executor.** Panel dipasang di `CoreGui`, jadi executor yang tidak mengizinkannya tidak akan menampilkan panel.
- "Roblox" adalah merek dagang Roblox Corporation, disebut hanya untuk menjelaskan kegunaan script. Proyek ini **tidak berafiliasi dengan Roblox**.

## Struktur berkas

```
livia-panel/
├── LiviaPanel.lua       # Script utama (UI + logika, satu berkas)
├── assets/
│   ├── banner.png       # Banner di atas README (1200x630, bisa jadi social preview)
│   ├── en/
│   │   └── banner.png   # Banner versi Inggris (dipakai README.en.md)
│   └── preview.png      # Tampilan panel
├── LICENSE              # MIT
├── README.md            # Bahasa Indonesia
└── README.en.md         # English
```

Isi `LiviaPanel.lua` dibagi per blok:

```
STATE                 Variabel S (ON/OFF) dan V (nilai) + tema warna T
FEATURE LOGIC         Heartbeat/Stepped untuk Speed, Jump, Fly, Ghost, ESP
TAP vs DRAG SYSTEM    Pembeda geser dan tekan (DRAG_THRESHOLD)
UI                    Header, baris fitur, tombol minimize/close
CLEANUP               Mematikan fitur, memutus koneksi, menghapus GUI
```

## Kontribusi

Masukan dan perbaikan sangat diterima lewat issue atau pull request. Sebelum membuka pull request, uji perubahan di executor pada game nyata: nyalakan dan matikan tiap fitur, geser panel, minimize lalu buka lagi, dan tutup dengan `X` lalu jalankan ulang untuk memastikan tidak ada panel dobel. Sebutkan executor dan game yang dipakai di deskripsi PR.

## Lisensi

Dirilis di bawah [Lisensi MIT](LICENSE).

---

<div align="center">
<sub>Livia Panel. Panel mobile untuk Roblox executor. Berjalan di sisi client.</sub>
</div>
