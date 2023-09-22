# OpenAI ChatGPT Telegram Bot
Telegram bot dengan APi ChatGPT yang bisa menjawab dan mempermudah proses kegiatan manusia dalam mengerjakan sesuatu.
# Cara Install
- Daftar akun OpenAI untuk mendapatkan APi Key di https://openai.com/api
- Masuk ke account -> APi dan kalian generate APi
- Buka telegram dan cari akun @botfather buat Bot dan simpan APi Tokennya
- install git dan python pip (replit not required)
  
  ubuntu/debian
  ```bash
  apt update
  apt install git python-pip
  ```
  termux
  ```sh
  pkg update
  pkg install git python-pip
  ```
  
- Clone repository atau bisa download Repository ini
```bash
git clone https://github.com/RiProG-id/OpenAI-Telegram-Bot
cd OpenAI-Telegram-Bot
```
- Edit APi Token dan APi Key sesuai dengan yang kalian buat
- Install Library / Requirements
```bash
pip install -r requirements.txt
```
- Jalankan program Bot nya
```bash
python openai-telegram.py
```
- Selamat anda berhasil membuat Bot ChatGPT

- Untuk pengguna replit jalankan sebelum program bot agar terus berjalan
```bash
node keep-alive.js
```
