# <h1 align="center">Laporan Praktikum Modul Dasar-Dasar Python untuk Sains Data</h1>
<p align="center">Yoka Romadani</p>

## Dasar Teori

Dasar-dasar Python Untuk Sains Data 
1. Variabel dan Tipe Data
   Variabel adalah tempat menyimpan data di memori. Nama variabel harus deskriptif dan 
mengikuti aturan penamaan, seperti menggunakan huruf, angka, atau underscore (_), dan 
tidak boleh diawali dengan angka.
```
x = 10
y = 3.14
z = "Data Science"
user_age = 20
pi_value = 3.14159
course_name = "Python for Data Science"
```
  Tipe data di Python adalah jenis nilai yang dapat diolah. Python mendukung beberapa tipe 
data dasar, antara lain:
• Integer (int): Bilangan bulat positif atau negatif, misalnya 10, -3.
• Float: Bilangan desimal atau pecahan, misalnya 3.14, -2.5.
• String (str): Rangkaian karakter yang didefinisikan dengan tanda kutip, misalnya 
"Data Science".
• Boolean (bool): Menyatakan nilai benar atau salah, yaitu True atau False
```
# Integers
age = 25
# Floats
height = 1.75
# Strings
name = "Agung"
# Booleans
is_student = True
print(type(age)) 
print(type(height)) 
print(type(name)) 
print(type(is_student))
```  
## Guided 

### 1. Buat Program yang menampilakan nama dan umur

```python
nama = "Yanto"
umur = 38
print(f"Nama : {nama} \nUmur : {umur}")
```
Kode program ini mencetak informasi tentang nama dan umur seseorang. Variabel nama dan umur diisi dengan nilai "Yanto" dan 38, kemudian dicetak menggunakan perintah print. Perintah print menggunakan sintaks f-string untuk memasukkan nilai variabel nama dan umur ke dalam teks yang akan dicetak. Hasilnya adalah teks "Nama : Yanto Umur : 38" yang dicetak ke layar.

### 2. Buat Program yang menampilakan perkalian 1 sampai 10

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
```
Kode program ini mencetak tabel perkalian dari 1 hingga 10. Perintah for pertama mengulangi proses dari 1 hingga 10, dan perintah for kedua juga mengulangi proses dari 1 hingga 10. Dalam setiap iterasi, program mencetak hasil perkalian antara nilai i dan j, yang merupakan hasil dari perintah i * j. Setelah mencetak hasil perkalian untuk satu baris, program mencetak baris kosong untuk memisahkan hasil perkalian antar baris. Hasilnya adalah tabel perkalian yang lengkap dari 1 hingga 10.

### 3. Buat fungsi yang menampilkan apakah suatu angka adalah bilangan prima

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
```
Kode program ini memeriksa apakah sebuah bilangan adalah bilangan prima atau tidak. Fungsi is_prime mengambil satu parameter n yang merupakan bilangan yang ingin diperiksa. Jika n kurang dari atau sama dengan 1, maka fungsi langsung mengembalikan False karena bilangan prima harus lebih besar dari 1.

Jika n lebih besar dari 1, maka fungsi melakukan perulangan dari 2 hingga akar kuadrat dari n untuk memeriksa apakah n dapat dibagi oleh bilangan lain. Jika n dapat dibagi oleh bilangan lain, maka fungsi mengembalikan False karena n bukan bilangan prima.

Jika n tidak dapat dibagi oleh bilangan lain, maka fungsi mengembalikan True karena n adalah bilangan prima. Pada contoh kode, kita memeriksa apakah bilangan 7 adalah bilangan prima, dan hasilnya adalah True karena 7 adalah bilangan prima.
## Unguided 

### 1.  Memecahkan Masalah Unik dengan Loop dan If-Else
Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, 
dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya:
```
1
2 3
5 7 11
13 17 19 23
...
```
Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan 
prima]

```python
def cek_prima(n):
    """Cek jika sebuah bilangan adalah prima"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_poligon_prima(n):
    """Generate poligon prima hingga n baris"""
    prima = []
    jumlah_prima = 0
    num = 2
    while jumlah_prima < n * (n + 1) // 2:
        if cek_prima(num):
            prima.append(num)
            jumlah_prima += 1
        num += 1

    poligon = []
    for i in range(1, n + 1):
        poligon.append(prima[:i])
        prima = prima[i:]

    return poligon

def cetak_poligon(poligon):
    """Cetak poligon dalam format yang diinginkan"""
    for baris in poligon:
        print(' '.join(str(x) for x in baris))

n = 4  
poligon = generate_poligon_prima(n)
cetak_poligon(poligon)
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20011423.png)


Kode di atas adalah membuat pola piramid dengan syarat penjumlahan bilangan prima sebelumnya.

### 2.  Membuat Fungsi dengan Syarat Spesifik
Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus 
mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. 
List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.

```python
def filter_elemen_indeks_ganjil(list1, list2):
    gabungan = list1 + list2
    
    hasil = [gabungan[i] for i in range(len(gabungan)) if i % 2 != 0 and gabungan[i] % 2 != 0]
    
    for i in range(len(gabungan)):
        if gabungan[i] % 2 != 0 and i % 2 == 0:
            hasil.append(gabungan[i])
    
    hasil.sort(reverse=True)
    
    return hasil

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

hasil = filter_elemen_indeks_ganjil(list1, list2)
print(hasil) 
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012211.png)

kode di atas merupakan fungsi yang menerima input dan angka. Dimana kode tersebut harus mengembalikan sebuah list yang berisi elemen dari dari dua list input yang memiliki indeks ganjil, dan ditutunkan secara menurun berdasarkan nilai elemen.
### 3.  Exception Handling dalam Konteks Nyata
 Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus:
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir

```python
saldo = 100000

def minta_pin():
    for i in range(3):
        pin = input("Masukkan PIN Anda: ")
        if pin == "1234": 
            return True
        else:
            print("PIN salah. Silakan coba lagi.")
    print("PIN salah sebanyak 3 kali. Transaksi dibatalkan.")
    return False

def minta_jumlah_penarikan():
    while True:
        try:
            jumlah_penarikan = int(input("Masukkan jumlah penarikan: "))
            if jumlah_penarikan <= 0:
                print("Jumlah penarikan harus lebih besar dari 0.")
            else:
                return jumlah_penarikan
        except ValueError:
            print("Jumlah penarikan harus berupa angka.")

def lakukan_penarikan(jumlah_penarikan):
    global saldo
    if jumlah_penarikan > saldo:
        print("Saldo tidak cukup. Transaksi dibatalkan.")
    else:
        saldo -= jumlah_penarikan
        print(f"Penarikan sebesar Rp {jumlah_penarikan} berhasil. Saldo akhir: Rp {saldo}")

if minta_pin():
    jumlah_penarikan = minta_jumlah_penarikan()
    lakukan_penarikan(jumlah_penarikan)
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-29%20215125.png)
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-29%20215156.png)


Kode program di atas adalah membuat program mengenai proses mesin Atm yang didalamnya meliputi 
1. meminta penguna memasukan pin(pasword) Atm sebanyak 3 kali
2. setelah pin benar maka program akan meminta jumlah penarikan yang di inginkan pengguna
3. jika salah makan akan keluar pemberitahuan seperti output gambar pertama
4. jika benar maka saldo akan berkurang dan program akan menampilkan jumlah saldo akhir

### 4.  Studi Kasus Pengelolaan Data
Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis 
sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.

```python
import csv

def baca_data_csv(file_name):
    data_mahasiswa = {}
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            nama = row[0]
            nilai = list(map(float, row[1:]))
            data_mahasiswa[nama] = nilai
            
    return data_mahasiswa

def hitung_rata_rata(data_mahasiswa):
    rata_rata = {}
    for nama, nilai in data_mahasiswa.items():
        rata_rata[nama] = sum(nilai) / len(nilai)
    return rata_rata

def mahasiswa_tertinggi_terendah(rata_rata):
    mahasiswa_tertinggi = max(rata_rata, key=rata_rata.get)
    mahasiswa_terendah = min(rata_rata, key=rata_rata.get)
    return mahasiswa_tertinggi, mahasiswa_terendah

def main():
    file_name = 'siswa_nilai.csv'
    data_mahasiswa = baca_data_csv(file_name)
    rata_rata = hitung_rata_rata(data_mahasiswa)
    mahasiswa_tertinggi, mahasiswa_terendah = mahasiswa_tertinggi_terendah(rata_rata)
    print("Rata-rata nilai tiap mahasiswa:")
    for nama, rata in rata_rata.items():
        print(f"{nama}: {rata:.2f}")
    
    print(f"\nMahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi} ({rata_rata[mahasiswa_tertinggi]:.2f})")
    print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terendah} ({rata_rata[mahasiswa_terendah]:.2f})")
if __name__ == "__main__":
    main()
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012420.png)
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012451.png)


Kode program di atas adalah membuat program mengenai bagaimana memasukan sebuah file csv kedalam dictionari dengan menggunakan fungsi import csv. Kemudian program tersebut menghitung rata-rata nilai mahasiswa dengan mengunakan fungsi def_baca_dictionari kemudian dilanjutkan dengan mengunakan fungsi def_hitung_rata-rata. Untuk menghitung Nilai tertinggi dan terendah program mengunakan def_terendah_dan_tertinggi. Untuk dapat menjalankan program maka ditambah fungsi def main. Dan pada hasil output dapat diketahui dari sebanyak 100 mahasiswa terdapat 7 mahasiswa yang mendapat nilai tertingi dan 5 mahasiswa yang mendapat nilai 50.

### 5.  Kombinasi Logika dan Kreativitas
Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih 
sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap 
tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih 
kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, 
tampilkan apakah pemain menang atau kalah.


```python
import random

angka_sebenarnya = random.randint(1, 100)
jumlah_percobaan = 5

print("Selamat datang di permainan tebak angka!")
print("Komputer telah memilih sebuah angka antara 1 hingga 100.")
print("Anda memiliki 5 kesempatan untuk menebak angka tersebut.")

for i in range(jumlah_percobaan):
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan == angka_sebenarnya:
        print("Selamat! Anda telah menebak angka dengan benar!")
        break
    elif tebakan < angka_sebenarnya:
        print("Angka yang Anda tebak terlalu kecil. Coba lagi!")
    else:
        print("Angka yang Anda tebak terlalu besar. Coba lagi!")

    jumlah_percobaan -= 1
    print(f"Anda memiliki {jumlah_percobaan} kesempatan lagi.")

if jumlah_percobaan == 0:
    print(f"Sayangnya, Anda telah kehabisan kesempatan. Angka yang benar adalah {angka_sebenarnya}.")
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012544.png)

Kode ini adalah permainan tebak angka sederhana yang ditulis dalam bahasa Python. Komputer secara acak memilih sebuah angka antara 1 dan 100, dan pengguna memiliki 5 kesempatan untuk menebak angka yang benar.

Permainan dimulai dengan mengimpor modul random, yang digunakan untuk menghasilkan angka acak. Kemudian, komputer menghasilkan angka integer acak antara 1 dan 100 dan mengassignnya ke variabel angka_sebenarnya (yang berarti "angka yang sebenarnya" dalam bahasa Indonesia). Jumlah kesempatan yang pengguna miliki untuk menebak angka yang benar diatur menjadi 5.

Loop permainan berjalan 5 kali, meminta pengguna untuk memasukkan tebakan mereka setiap kali. Program memeriksa apakah tebakan pengguna sama dengan angka yang benar, dan jika demikian, program mencetak pesan sukses dan keluar dari loop. Jika tebakan pengguna terlalu kecil, program mencetak pesan petunjuk yang menunjukkan bahwa angka yang benar lebih tinggi. Jika tebakan pengguna terlalu besar, program mencetak pesan petunjuk yang menunjukkan bahwa angka yang benar lebih kecil. Setelah setiap tebakan, program mengurangi jumlah kesempatan yang tersisa sebanyak 1 dan mencetak jumlah kesempatan yang tersisa.

Jika pengguna kehabisan kesempatan, program mencetak pesan game over yang mengungkapkan angka yang benar. Itu saja! Saya harap penjelasan ini membantu Anda memahami kode.

Kode program di atas adalah membuat program mengenai 

### 6. Rekursi yang Tidak Biasa
Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan 
bilangan seperti berikut ini:
```
Input: n = 4
Output: 1, 1, 2, 6, 24
```
Fungsi ini harus menggunakan konsep rekursi untuk menghitung faktorial setiap angka hingga `n`

```python
def urutan_bilangan(n):
    if n == 1:
        return [1]
    else:
        urutan_sebelumnya = urutan_bilangan(n - 1)
        urutan_sebelumnya.append(urutan_sebelumnya[-1] * n)
        return urutan_sebelumnya
n = 4
print(urutan_bilangan(n))  
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012607.png)

Kode program ini mendefinisikan fungsi urutan_bilangan yang menghasilkan urutan bilangan faktorial. Fungsi ini mengambil satu parameter n yang menentukan panjang urutan bilangan yang dihasilkan.

Jika n sama dengan 1, fungsi akan mengembalikan list yang berisi hanya satu elemen, yaitu 1. Namun, jika n lebih besar dari 1, fungsi akan memanggil dirinya sendiri dengan parameter n-1 untuk menghasilkan urutan bilangan sebelumnya. Kemudian, fungsi akan menambahkan elemen baru ke urutan sebelumnya dengan mengalikan elemen terakhir urutan sebelumnya dengan n. Hasilnya adalah urutan bilangan faktorial yang dihasilkan.

Pada contoh kode, kita memanggil fungsi urutan_bilangan dengan parameter n=4, sehingga fungsi akan menghasilkan urutan bilangan faktorial untuk n=4, yaitu [1, 2, 6, 24].

### 7. Pemrograman dengan Algoritma Greedy
Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan 
jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi 
minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. Namun, program Anda 
harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.

```python
def minimum_coin_change(jumlah_uang, nilai_koin):
    tabel = [float('inf')] * (jumlah_uang + 1)
    tabel[0] = 0

    for koin in nilai_koin:
        for i in range(koin, jumlah_uang + 1):
            tabel[i] = min(tabel[i], tabel[i - koin] + 1)

    if tabel[jumlah_uang] == float('inf'):
        print("Tidak ada kombinasi koin yang dapat mencapai jumlah uang tersebut.")
    else:
        print("Kombinasi minimum koin yang diperlukan:")
        i = jumlah_uang
        while i > 0:
            for koin in nilai_koin:
                if tabel[i] == tabel[i - koin] + 1:
                    print(f"{koin} koin")
                    i -= koin
                    break

jumlah_uang = int(input("Masukkan jumlah uang: "))
nilai_koin = list(map(int, input("Masukkan nilai koin (pisahkan dengan spasi): ").split()))
minimum_coin_change(jumlah_uang, nilai_koin)
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012622.png)

Kode program ini mendefinisikan fungsi minimum_coin_change yang menghitung kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tertentu. Fungsi ini mengambil dua parameter: jumlah_uang yang menentukan jumlah uang yang ingin dicapai, dan nilai_koin yang merupakan list nilai koin yang tersedia.

Fungsi ini menggunakan teknik dinamis untuk menghitung kombinasi minimum koin. Pertama, fungsi membuat tabel yang berisi jumlah minimum koin yang diperlukan untuk mencapai setiap jumlah uang dari 0 hingga jumlah_uang. Kemudian, fungsi iterasi melalui setiap nilai koin dan memperbarui tabel dengan jumlah minimum koin yang diperlukan untuk mencapai setiap jumlah uang.

Setelah tabel selesai dihitung, fungsi memeriksa apakah ada kombinasi koin yang dapat mencapai jumlah uang yang diinginkan. Jika tidak, fungsi mencetak pesan bahwa tidak ada kombinasi koin yang dapat mencapai jumlah uang tersebut. Jika ada, fungsi mencetak kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut.

Pada contoh kode, kita meminta pengguna untuk memasukkan jumlah uang dan nilai koin yang tersedia. Kemudian, kita memanggil fungsi minimum_coin_change dengan parameter yang dimasukkan oleh pengguna untuk menghitung kombinasi minimum koin yang diperlukan.

### 8.  Kombinasi String dan Manipulasi List
Buat sebuah program yang menerima string dari pengguna dan mengonversi string 
tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:
```
Input: "Saya suka Python"
Output: ["ayaS", "akus", "nohtyP"]
``

```python
def string_to_reversed_words(input_string):
    kata_kata = input_string.split()

    kata_kata_terbalik = [kata[::-1] for kata in kata_kata]

    return kata_kata_terbalik

input_string = input("Masukkan string: ")
output = string_to_reversed_words(input_string)
print(output)
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012643.png)

Kode program ini mendefinisikan fungsi string_to_reversed_words yang mengubah string menjadi list kata-kata yang dibalik. Fungsi ini mengambil satu parameter input_string yang merupakan string yang ingin diubah.

Fungsi ini bekerja dengan cara membagi string menjadi list kata-kata menggunakan metode split(). Kemudian, fungsi menggunakan list comprehension untuk membuat list baru yang berisi kata-kata yang dibalik. Setiap kata dibalik menggunakan sintaks kata[::-1].

Akhirnya, fungsi mengembalikan list kata-kata yang dibalik. Pada contoh kode, kita meminta pengguna untuk memasukkan string, kemudian kita memanggil fungsi string_to_reversed_words dengan parameter string yang dimasukkan oleh pengguna. Hasilnya adalah list kata-kata yang dibalik, yang kemudian kita cetak ke layar.

### 9.  Konsep Class dan Object-Oriented Programming
Buat class bernama `Buku` yang memiliki atribut `judul`, `penulis`, dan `tahun_terbit`. 
Buat method dalam class untuk menampilkan informasi buku, serta method untuk menghitung usia 
buku berdasarkan tahun saat ini. Buatlah 3 objek dari class `Buku` dan tampilkan informasi serta 
usia masing-masing buku
```python
from datetime import date

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def hitung_usia(self):
        tahun_saat_ini = date.today().year
        usia = tahun_saat_ini - self.tahun_terbit
        return usia

buku1 = Buku("Algoritma Python", "Ruseli", 2010)
buku2 = Buku("Dasar-Dasar Algoritma", "Willy Smith", 2015)
buku3 = Buku("Pengenalan Machine Learning", "Cole Ashley", 2020)

print("Informasi Buku 1:")
buku1.tampilkan_informasi()
print(f"Usia: {buku1.hitung_usia()} tahun")
print()

print("Informasi Buku 2:")
buku2.tampilkan_informasi()
print(f"Usia: {buku2.hitung_usia()} tahun")
print()

print("Informasi Buku 3:")
buku3.tampilkan_informasi()
print(f"Usia: {buku3.hitung_usia()} tahun")
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012736.png)

Kode program ini mendefinisikan sebuah kelas Buku yang memiliki tiga atribut: judul, penulis, dan tahun_terbit. Kelas ini juga memiliki dua metode: tampilkan_informasi yang mencetak informasi buku, dan hitung_usia yang menghitung usia buku berdasarkan tahun terbit dan tahun saat ini.

Pada contoh kode, kita membuat tiga objek buku: buku1, buku2, dan buku3, dengan judul, penulis, dan tahun terbit yang berbeda-beda. Kemudian, kita mencetak informasi setiap buku menggunakan metode tampilkan_informasi, dan juga mencetak usia setiap buku menggunakan metode hitung_usia.

Metode hitung_usia bekerja dengan cara mengambil tahun saat ini menggunakan fungsi date.today().year, kemudian menghitung usia buku dengan mengurangi tahun terbit dari tahun saat ini. Hasilnya adalah usia buku dalam tahun, yang kemudian kita cetak ke layar.

### 10.  Algoritma dengan Persyaratan Logika Khusus
Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan 
modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai 
yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa 
ditemukan
```python
def pencarian_biner(list_angka, target):
    if target % 2 != 0:
        return "Nilai yang dicari tidak bisa ditemukan karena merupakan angka ganjil"

    awal = 0
    akhir = len(list_angka) - 1

    while awal <= akhir:
        tengah = (awal + akhir) // 2
        if list_angka[tengah] == target:
            return f"Nilai {target} ditemukan pada indeks {tengah}"

        elif target < list_angka[tengah]:
            akhir = tengah - 1

        else:
            awal = tengah + 1

    return "Nilai yang dicari tidak ditemukan"

list_angka = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
print(pencarian_biner(list_angka, target))  

target = 11
print(pencarian_biner(list_angka, target))  

target = 22
print(pencarian_biner(list_angka, target))  
```
#### Output:
![image](https://github.com/yokaroo/Laporan-Praktikum-Infrastruktur-dan-Platform-Untuk-Sains-Data-1/blob/main/Modul%201/Screenshot%202024-09-30%20012747.png)

Kode program ini melakukan pencarian nilai dalam list angka menggunakan metode pencarian biner. Fungsi pencarian_biner memeriksa apakah nilai target adalah angka genap, jika tidak maka mengembalikan pesan bahwa nilai tidak ditemukan.

Jika nilai target adalah angka genap, fungsi melakukan pencarian biner dengan membagi list angka menjadi dua bagian dan memeriksa nilai tengah. Jika nilai tengah sama dengan nilai target, fungsi mengembalikan indeks nilai target. Jika nilai target tidak ditemukan, fungsi mengembalikan pesan bahwa nilai tidak ditemukan.

Pada contoh kode, kita melakukan pencarian nilai 12, 11, dan 22 dalam list angka. Hasilnya adalah indeks nilai 12, pesan bahwa nilai 11 tidak ditemukan karena merupakan angka ganjil, dan pesan bahwa nilai 22 tidak ditemukan.
## Kesimpulan
Bahasa pemprograman merupakan adalah suatu komando atau perintah yang dibuat manusia untk membuat komputer menjadi memiliki fungsi tertentu[1]. Dengan belajar Dasar-dasar python untuk sains data kita dapat mengetahui beerbagai macam tipe data dan variabel yang ada dalam bahasa pemrogaman python.

## Referensi
[1] Wimawan, R. B. (2019, April 11). Tipe Data Sederhana. https://doi.org/10.31219/osf.io/vwf52
