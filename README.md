# Kelompok 5 Kelas C
Tugas Pemrograman Komputer dan Algoritma Teknik Industri 2024 Kelas C

## Anggota Kelompok:
1. **Rinka Amelia Gifanti** (I0324099)
2. **Danaila Aisha Nandita Azzahra** (I0324104)
3. **Rahma Nur Citantya** (I0324108)
4. **Rangga Among Gati** (I0324109)

## Tema: Sistem Pencatat Pengeluaran Harian

## Deskripsi Singkat:
Sistem ini dirancang untuk membantu pengguna, terutama mahasiswa untuk mencatat pemasukan dan pengeluaran harian serta mengelola anggaran. Pengguna dapat menginput data pemasukan, menentukan alokasi tabungan, dan menghitung anggaran harian. Selain itu, sistem memungkinkan pencatatan pengeluaran, memverifikasi kelengkapan data, serta memberikan notifikasi jika pengeluaran melebihi anggaran. Data yang tercatat akan digunakan untuk membuat laporan keuangan yang mencakup total pengeluaran, kategori, dan sisa anggaran, yang kemudian dikirimkan kepada pengguna.

## Fitur:
1. Pencatatan pengeluaran harian sekaligus kategorisasi pengeluaran. 
2. Sistem dapat memberi laporan dan analisis mingguan atau bulanan mengenai total pengeluaran. 
3. Memiliki fitur pengingat untuk mencatat pengeluaran serta pengguna dapat menetapkan anggaran yang sesuai dengan batasan.

**Flowchart Sistem Pencatat Pengeluaran Harian**
![Revisi Flowchart Sistem](https://github.com/user-attachments/assets/e16ee1e6-4d74-4044-9910-dd8a035b7164)


## Library yang Ditambahkan:
1. **Pastikan Python Terinstal dengan GUI/Tkinter**  
   Program ini menggunakan antarmuka grafis berbasis library `tkinter`, yang biasanya sudah termasuk dalam instalasi default Python. Jika Python tidak mendukung GUI/Tkinter, pastikan kita menginstal ulang Python dengan fitur lengkap.  

2. **Instal Library yang Dibutuhkan**  
   Beberapa library eksternal digunakan dalam program ini, yaitu:  
   **`pillow`** , **`pandas`** , **`openpyxl`** , **`tkcalendar`**

   Kita dapat menginstal semua library ini dengan mengetikkan perintah berikut di terminal atau command prompt:  
   ```bash
   pip install pillow pandas openpyxl tkcalendar
   ```

3. **Pastikan File Gambar Tersedia**  
   Program tersebut memerlukan file gambar dan pastikan file gambar berada di direktori yang sama dengan file program utama. Jika file gambar tidak ditemukan, beberapa bagian antarmuka mungkin tidak akan tampil dengan benar.

4. **Pastikan File `database_module.py` Tersedia**  
   Program menggunakan file `database_module.py` untuk mengelola data di file Excel. Berikut adalah isi file `database_module.py` yang sesuai dengan program ini:  
   ```python
   import pandas as pd

   DATABASE_FILE = "data.xlsx"  # File tempat menyimpan data

   # Fungsi untuk menyimpan data baru ke file Excel
   def simpan_data(tanggal, pemasukan, pengeluaran, keterangan, anggaran, sisa_anggaran):
       try:
           # Membaca data yang sudah ada di file Excel
           df = pd.read_excel(DATABASE_FILE)
       except FileNotFoundError:
           # Jika file belum ada, membuat DataFrame baru
           kolom = ['Tanggal', 'Pemasukan', 'Pengeluaran', 'Keterangan', 'Anggaran Mingguan', 'Sisa Anggaran']
           df = pd.DataFrame(columns=kolom)

       # Menambahkan data baru ke DataFrame
       data_baru = {
           'Tanggal': tanggal,
           'Pemasukan': pemasukan,
           'Pengeluaran': pengeluaran,
           'Keterangan': keterangan,
           'Anggaran Mingguan': anggaran,
           'Sisa Anggaran': sisa_anggaran
       }
       df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)

       # Menyimpan kembali ke file Excel
       df.to_excel(DATABASE_FILE, index=False)
   ```

   Pastikan file `database_module.py` berada dalam direktori yang sama dengan program utama.

5. **Setelah Semua Langkah Dilakukan**  
   Jika semua persyaratan di atas sudah terpenuhi, kita dapat menjalankan program ini tanpa kendala.
