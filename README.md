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
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 3. Unduh dan Konfigurasi Mailu
Pergi ke https://setup.mailu.io/2024.06/

#### Step 1 – Initial configuration:

- Mailu storage path: /mailu
- Main mail domain and server display name: domainmu.com (your domain).
- Postmaster local part: admin
- Choose how you wish to handle security TLS certificates: letsencrypt
- Website name: Web Shanks (your preferred name).
- Linked Website URL: https://domainmu.com
- Enable the admin UI: yes

#### Step 2 – Pick some features:

- Enable Web email client: roundcube
- Enable the antivirus service: yes
- Enable the webdav service: yes
- Enable fetchmail: yes
- Enable oletools: yes
- Enable Tika: yes


#### Step 3 – expose Mailu to the world:

- IPv4 listen address: your IPv4
- Enable an internal DNS resolver (unbound): yes
- Step 3 - expose Mailu to the world

#### Step 4 - setelah itu ikuti petunjuk install di setup.mailu.io

### 4.Configure Mailu Catch-All
To set up a catch-all email, do the following:

- Open Mailu admin panel
- Go to Aliases
- Add an alias with Localpart = %
- Destination should be log@domain.com
- Check the box "Use SQL LIKE Syntax"
- Now, any email sent to any address under your domain will be redirected to log@domain.com


## Menjalankan `Private.py` di Termux

### 1. Instalasi Termux dan Dependensi
```bash
pkg update && pkg upgrade -y
pkg install python git nano -y
git clone https://github.com/dalungid/mscrt.git
cd mscrt
pip install -r requirements.txt
```
### 2. Konfigurasi .env
```bash
nano .env
```
- EMAIL_PASSWORD=your-email-password
- IMAP_SERVER=your-imap-server
- IMAP_PORT=993
- CATCHALL_EMAIL=log@domain.com
- DOMAINS=domainmu.com
- USER_AGENTS=disini
- **LU JUGA BISA LIHAT CONTOH *.env.sample* didalam folder mscrt**
### 3. Jalankan `Private.py`
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
```