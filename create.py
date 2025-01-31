import os
import time
import sys
import re
import json
import random
import string
import hashlib
import threading
from queue import Queue
from faker import Faker
import requests

# Warna Terminal
P = "\x1b[38;5;231m"  # Putih
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"   # Hijau
A = "\x1b[38;5;248m"  # Abu
B = "\x1b[38;5;21m"   # Biru

# Konfigurasi
fake = Faker()
bulan = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
    5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}

# Data Nama Indonesia Gen-Z
male_names = ["Arkan", "Bintang", "Daffa", "Fathir", "Naufal", 
             "Raihan", "Zidan", "Genta", "Bagas", "Kinan"]
female_names = ["Aisyah", "Citra", "Zahra", "Nadia", "Salsabila", 
               "Wulan", "Kirana", "Bunga", "Dewi", "Indah"]
last_names = ["Putra", "Pratama", "Wijaya", "Kusuma", "Hidayat",
             "Saputra", "Ramadhani", "Maulana", "Anggara", "Kurniawan"]

def logo():
    print(f"""{B}
    ╔═╗╔╗╔╔═╗╦ ╦  ╔═╗╔═╗╔╦╗╔═╗╦═╗
    ║ ╦║║║║╣ ║║║  ╠═╝╠═╣║║║║╣ ╠╦╝
    ╚═╝╝╚╝╚═╝╚╩╝  ╩  ╩ ╩╩ ╩╚═╝╩╚═
    {A}› Github: @jatintiwari0   {H}› By: JATIN TIWARI
    {M}› Proxy Support: @coopers-lab{P}""")
    print('\n' + '\x1b[38;5;208m⇼'*50 + P)

class ProxyManager:
    def __init__(self):
        self.valid_proxies = []
        self.load_proxies()
        
    def load_proxies(self):
        try:
            with open('proxies.txt', 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            self.test_proxies(proxies)
        except FileNotFoundError:
            print(f"{M}✖ File proxies.txt tidak ditemukan!{P}")
    
    def test_proxies(self, proxies):
        q = Queue()
        for proxy in proxies:
            q.put(proxy)
            
        for _ in range(20):
            t = threading.Thread(target=self.worker_test_proxy, args=(q,))
            t.daemon = True
            t.start()
            
        q.join()
        
    def worker_test_proxy(self, q):
        while True:
            proxy = q.get()
            if self.test_single_proxy(proxy):
                self.valid_proxies.append(proxy)
            q.task_done()
    
    def test_single_proxy(self, proxy):
        try:
            res = requests.get(
                'http://ipinfo.io/json',
                proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'},
                timeout=10
            )
            return res.status_code == 200
        except:
            return False

class FacebookAccountCreator:
    def __init__(self):
        self.api_key = "882a8490361da98702bf97a021ddc14d"
        self.secret = "62f8ce9f74b12f84c123cc23437a4a32"
        self.proxy_manager = ProxyManager()
    
    def generate_email(self):
        if not self.proxy_manager.valid_proxies:
            return None, None
            
        proxy = random.choice(self.proxy_manager.valid_proxies)
        proxy_dict = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        
        try:
            # Dapatkan domain email
            domains = requests.get(
                "https://api.mail.tm/domains",
                proxies=proxy_dict
            ).json()['hydra:member']
            
            domain = random.choice(domains)['domain']
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            email = f"{username}@{domain}"
            
            # Buat akun email
            password = hashlib.md5(os.urandom(32)).hexdigest()[:8]
            response = requests.post(
                "https://api.mail.tm/accounts",
                json={"address": email, "password": password},
                headers={"Content-Type": "application/json"},
                proxies=proxy_dict
            )
            
            if response.status_code == 201:
                return email, password, proxy_dict
            return None, None, None
            
        except Exception as e:
            print(f"{M}✖ Error membuat email: {str(e)}{P}")
            return None, None, None
    
    def register_facebook(self, email, password, first, last, gender, proxy):
        params = {
            'api_key': self.api_key,
            'attempt_login': True,
            'birthday': fake.date_of_birth(minimum_age=17, maximum_age=25).strftime('%Y-%m-%d'),
            'client_country_code': 'ID',
            'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
            'fb_api_req_friendly_name': 'registerAccount',
            'firstname': first,
            'lastname': last,
            'email': email,
            'gender': gender if gender in ['M','F'] else random.choice(['M','F']),
            'locale': 'id_ID',
            'password': password,
            'reg_instance': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
        }
        
        # Generate signature
        sig = ''.join(f'{k}={v}' for k,v in sorted(params.items()))
        params['sig'] = hashlib.md5((sig + self.secret).encode()).hexdigest()
        
        try:
            response = requests.post(
                'https://b-api.facebook.com/method/user.register',
                data=params,
                proxies=proxy,
                timeout=20
            )
            data = response.json()
            
            if 'error' in data:
                print(f"{M}✖ Gagal registrasi: {data['error']['message']}{P}")
                return None
                
            return {
                'uid': data.get('new_user_id', 'N/A'),
                'token': data.get('session_info', {}).get('access_token', 'N/A')
            }
        except Exception as e:
            print(f"{M}✖ Error API Facebook: {str(e)}{P}")
            return None
    
    def get_cookies(self, email, password, proxy):
        session = requests.Session()
        session.proxies = proxy
        try:
            # Dapatkan parameter login
            login_page = session.get('https://m.facebook.com/login/')
            lsd = re.search('name="lsd" value="(.*?)"', login_page.text).group(1)
            
            # Proses login
            login_response = session.post(
                'https://m.facebook.com/login/',
                data={
                    'lsd': lsd,
                    'email': email,
                    'pass': password
                }
            )
            
            if 'c_user' in session.cookies:
                return {
                    'c_user': session.cookies.get('c_user'),
                    'xs': session.cookies.get('xs')
                }
            return None
        except Exception as e:
            print(f"{M}✖ Error mendapatkan cookie: {str(e)}{P}")
            return None

class Menu:
    def __init__(self):
        self.creator = FacebookAccountCreator()
        self.run()
    
    def run(self):
        while True:
            logo()
            print(f"{A}[{H}1{A}] {P}Buat Akun Baru")
            print(f"{A}[{H}2{A}] {P}Cek Hasil")
            print(f"{A}[{H}0{A}] {P}Keluar\n")
            
            choice = input(f" {M}➤ {P}Pilih opsi: {H}")
            
            if choice == '1':
                self.create_account_menu()
            elif choice == '2':
                self.check_results()
            elif choice == '0':
                exit(f"\n{M}✖ {P}Program dihentikan{P}")
            else:
                print(f"{M}✖ Pilihan tidak valid!{P}")
                time.sleep(1)
    
    def create_account_menu(self):
        print(f"\n{A}──[{P}PENGATURAN AKUN{A}]──{P}")
        
        # Pilih Gender
        gender = input(f"{A}[{H}?{A}] {P}Gender (L/P/R): {H}").upper()
        if gender not in ['L', 'P', 'R']:
            gender = 'R'
        
        # Generate Nama
        name_choice = input(f"{A}[{H}?{A}] {P}Nama (R/M): {H}").upper()
        if name_choice == 'M':
            first = input(f" {M}➤ {P}Nama Depan: {H}")
            last = input(f" {M}➤ {P}Nama Belakang: {H}")
        else:
            if gender == 'L':
                first = random.choice(male_names)
            elif gender == 'P':
                first = random.choice(female_names)
            else:
                first = random.choice(male_names + female_names)
            last = random.choice(last_names)
        
        # Generate Password
        pass_choice = input(f"{A}[{H}?{A}] {P}Password (R/M): {H}").upper()
        if pass_choice == 'M':
            password = input(f" {M}➤ {P}Password: {H}")
            while len(password) < 6:
                print(f"{M}✖ Password minimal 6 karakter!{P}")
                password = input(f" {M}➤ {P}Password: {H}")
        else:
            password = hashlib.md5(str(time.time()).encode()).hexdigest()[:10]
        
        # Proses Pembuatan Akun
        self.create_account(first, last, password, gender)
    
    def create_account(self, first, last, password, gender):
        print(f"\n{H}➤ {P}Memulai proses registrasi...{A}")
        
        email, email_pass, proxy = self.creator.generate_email()
        if not email:
            print(f"{M}✖ Gagal membuat email!{P}")
            return
            
        fb_data = self.creator.register_facebook(
            email=email,
            password=password,
            first=first,
            last=last,
            gender=gender,
            proxy=proxy
        )
        
        if fb_data:
            cookies = self.creator.get_cookies(email, password, proxy)
            self.show_result(
                name=f"{first} {last}",
                uid=fb_data['uid'],
                email=email,
                password=password,
                cookies=cookies
            )
    
    def show_result(self, **data):
        print(f"\n{H}✔ {P}Registrasi Berhasil!")
        print(f"{A}├ Nama   : {H}{data['name']}")
        print(f"{A}├ ID     : {H}{data['uid']}")
        print(f"{A}├ Email  : {H}{data['email']}")
        print(f"{A}├ Pass   : {H}{data['password']}")
        print(f"{A}└ Cookie : {H}{json.dumps(data['cookies'])}{P}\n")
        
        # Simpan ke file
        with open('results.txt', 'a') as f:
            f.write(json.dumps(data) + '\n')
    
    def check_results(self):
        try:
            with open('results.txt', 'r') as f:
                results = [json.loads(line) for line in f.readlines()]
            
            print(f"\n{A}──[{P}AKUN YANG BERHASIL DIBUAT{A}]──{P}")
            for idx, acc in enumerate(results, 1):
                print(f"{A}[{H}{idx}{A}] {acc['email']} | {H}{acc['password']}")
            input(f"\n{M}➤ {P}Tekan enter untuk kembali...")
        except FileNotFoundError:
            print(f"{M}✖ Belum ada hasil!{P}")
            time.sleep(1)

if __name__ == '__main__':
    try:
        Menu()
    except KeyboardInterrupt:
        exit(f"\n{M}✖ {P}Program dihentikan{P}")