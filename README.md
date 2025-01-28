# README

## Private.py

`Private.py` adalah script Python yang digunakan untuk mengelola email menggunakan Mailu yang diinstal pada VPS. Script ini harus dijalankan di Termux dengan koneksi data seluler (bukan WiFi). Proxy resident juga harus ditambahkan ke `data.txt`.

## Instalasi Mailu di VPS

### 1. Persyaratan VPS
- **Minimal Spesifikasi VPS:**
  - 1 vCPU
  - 2 GB RAM
  - 20 GB Storage
  - Sistem Operasi: Ubuntu 22.04 / Debian 11

### 2. Instalasi Docker dan Docker Compose
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
sudo systemctl start docker
```

### 3. Unduh dan Konfigurasi Mailu
```bash
git clone https://github.com/Mailu/Mailu.git
cd Mailu/setup
python3 setup.py
```
Ikuti petunjuk dan masukkan konfigurasi yang sesuai untuk domain Anda (`domain.com`).

### 4. Jalankan Mailu
```bash
docker-compose up -d
```

## Menjalankan `Private.py` di Termux

### 1. Instalasi Termux dan Dependensi
```bash
pkg update && pkg upgrade -y
pkg install python git nano -y
pip install -r requirements.txt
```

### 2. Jalankan `Private.py`
```bash
python Private.py
```

## Konfigurasi Tambahan
- Pastikan `data.txt` telah ditambahkan dengan proxy resident.
- Gunakan koneksi **data seluler**, bukan WiFi, saat menjalankan `Private.py` di Termux.
- Pastikan server Mailu di VPS telah dikonfigurasi dengan benar.

## Catatan Penting
- Gunakan hanya untuk tujuan yang sah.
- Pastikan domain yang digunakan sudah dikonfigurasi dengan benar untuk Mailu.
- Periksa log jika ada error dengan menjalankan:
```bash
docker-compose logs --tail=50
