# Livia Panel

Panel sederhana untuk Roblox executor (dirancang untuk layar HP, diuji konsepnya di Delta).

## Fitur

| Fitur | Pengaturan | Keterangan |
|---|---|---|
| Speed | angka + ON/OFF | Kecepatan lari |
| Jump | angka + ON/OFF | Tinggi lompat |
| Fly | angka + ON/OFF | Terbang, angka = kecepatan |
| Ghost | ON/OFF | Tembus tembok (noclip) |
| ESP Player | ON/OFF | Pemain lain terlihat tembus pandang |

## Cara pakai

Salin isi `LiviaPanel.lua` ke executor, atau jalankan lewat loadstring:

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/akndrn000/LiviaPanel.lua/main/LiviaPanel.lua"))()
```

Ganti `USERNAME` dan `REPO` dengan akun dan nama repository kamu.

## Kontrol

- Geser panel lewat header, latar panel, atau baris mana pun. Tombol tidak aktif saat digeser, hanya saat ditekan singkat.
- `-` meminimize panel menjadi bulatan **L**. Tekan bulatan itu untuk membuka lagi.
- `X` mematikan semua fitur dan menutup panel.
- Angka di kotak bisa diubah saat fitur sedang ON dan langsung berlaku.
- Fly: gunakan joystick untuk bergerak, arahkan kamera ke atas atau ke bawah untuk naik atau turun.

## Catatan

- Beberapa game memiliki anti-cheat. Jika speed atau jump terasa ditarik balik, gunakan angka yang lebih kecil.
- Script ini hanya berjalan di sisi client.
- Menggunakan script di game bisa melanggar Terms of Use Roblox dan berisiko akun terkena sanksi. Gunakan dengan risiko sendiri.
