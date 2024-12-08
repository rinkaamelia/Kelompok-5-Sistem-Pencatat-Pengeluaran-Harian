# Kelompok 5 Kelas C
Tugas Pemrograman Komputer dan Algoritma Teknik Industri 2024 Kelas C

## Anggota Kelompok:
1. **Rinka Amelia Gifanti** (I0324099)
2. **Danaila Aisha Nandita Azzahra** (I0324104)
3. **Rahma Nur Citantya** (I0324108)
4. **Rangga Among Gati** (I0324109)

# Tema: Sistem Pencatat Pengeluaran Harian

## Deskripsi Singkat:
Sistem ini dirancang untuk membantu pengguna, terutama mahasiswa untuk mencatat pemasukan dan pengeluaran harian serta mengelola anggaran. Pengguna dapat menginput data pemasukan, menentukan alokasi tabungan, dan menghitung anggaran harian. Selain itu, sistem memungkinkan pencatatan pengeluaran, memverifikasi kelengkapan data, serta memberikan notifikasi jika pengeluaran melebihi anggaran. Data yang tercatat akan digunakan untuk membuat laporan keuangan yang mencakup total pengeluaran, kategori, dan sisa anggaran, yang kemudian dikirimkan kepada pengguna.

## Fitur:
1. Pencatatan pengeluaran harian sekaligus kategorisasi pengeluaran. 
2. Sistem dapat memberi laporan dan analisis mingguan atau bulanan mengenai total pengeluaran. 
3. Memiliki fitur pengingat untuk mencatat pengeluaran serta pengguna dapat menetapkan anggaran yang sesuai dengan batasan.

## **Flowchart Sistem Pencatat Pengeluaran Harian**
![REVISI FLOWCHART](https://github.com/user-attachments/assets/e46ff424-e7ed-4552-97da-fd902c260d0a)
**Cara Menggunakan**
- Mulai (start) proses dimulai dengan titik ini sebagai titik awal dari sebuah sistem.
- Start screen akan menampilkan 2 pilihan, mulai atau keluar.
- Jika memilih tombol mulai, maka user akan masuk ke menu utama. Jika memilih tomboh keluar, maka user akan keluar dari program tersebut.
- Pada menu utama terdapat 4 pilihan yaitu alokasi, pengeluaran, laporan bulanan, dan kembali.
- Input pilihan
- Jika memilih 1 (alokasi), maka muncul isian tanggal, jumlah pemasukan, keterangan, dan tombol kembali. Jika user memilih tombol kembali, user akan kembali ke menu utama. Jika tidak, user akan tetap berada di laman alokasi. Input tanggal, jumlah pemasukan, dan keterangan. Jika data tidak lengkap maka akan menampilkan notifikasi "Data tidak lengkap" dan akan dikembalikan ke bagian input data. Jika data lengkap, maka dilakukan pengecekan jumlah pemasukan berupa angka. Jika tidak berupa angka maka akan menampilkan notifikasi "Jumlah harus angka" dan dikembalikan ke bagian input data. Jika jumlah berupa angka, maka sistem akan memproses jumlah anggaran mingguan, lalu data tersebut akan disimpan dalam database. Kemudian muncul notifikasi "Anggaran Mingguan XXX". Jika menutup notifikasi maka akan kembali ke menu utama, jika tidak menutup notifikasi maka akan tetap memunculkan notifikasi tersebut.
- Jika memilih 2 (pengeluaran), maka muncul isian tanggal, pengeluaran, keterangan, dan tombol kembali. Jika user memilih tombol kembali, user akan kembali ke menu utama. Jika tidak, user akan tetap berada di laman pengeluaran. Input tanggal, pengeluaran, dan keterangan. Jika data tidak lengkap maka akan menampilkan notifikasi "Data tidak lengkap" dan akan dikembalikan ke bagian input data. Jika data lengkap, maka dilakukan pengecekan jumlah pemasukan berupa angka. Jika tidak berupa angka maka akan menampilkan notifikasi "Jumlah harus angka" dan dikembalikan ke bagian input data. Jika jumlah berupa angka, maka sistem akan memproses sisa anggaran, lalu data tersebut akan disimpan dalam database. Kemudian muncul notifikasi "Sisa Anggaran XXX". Jika menutup notifikasi maka akan kembali ke menu utama, jika tidak menutup notifikasi maka akan tetap memunculkan notifikasi tersebut.
- Jika memilih 3 (laporan bulanan), maka muncul isian tanggal dan tombol kembali. Jika user memilih tombol kembali, user akan kembali ke menu utama. Jika tidak, user akan tetap berada di laman laporan bulanan. Input tanggal untuk menyaring database yang akan ditampilkan. Jika tanggal tidak valid maka tidak akan memunculkan anggaran dan akan kembali ke input tanggal. Jika tanggal valid, maka data akan disaring berdasarkan data yang dipilih. Jika data tidak ditemukan maka tidak akan memunculkan anggaran dan dikembalikan ke bagian input tanggal. Jika data ditemukan, maka sistem akan menampilkan laporan dalam bentuk tabel (treeview) yang berisi tanggal, pemasukan, pengeluaran, kategori, dan sisa anggaran. Kemudian sistem akan menampilkan total pemasukan, pengeluaran, dan total sisa anggaran.
- Jika memilih 3 (kembali), maka akan kembali ke start screen yang menampilkan tombol mulai dan keluar. Jika tidak memilih 3 maka user akan tetap berada di menu utama tersebut.
- Selesai (end) untuk proses yang telah berakhir.
## Library yang Ditambahkan:
### **Library Standar Python**
1. **`tkinter`**
   - Digunakan untuk antarmuka grafis (GUI). Biasanya sudah termasuk dalam instalasi Python standar.

### **Library Eksternal**
1. **`Pillow`**
   - Memungkinkan pemrosesan gambar, seperti menyesuaikan ukuran gambar dan menampilkannya pada GUI.
   - Dapat dipasang menggunakan perintah:  
     ```bash
     pip install pillow
     ```

2. **`pandas`**
   - Berguna untuk mengelola data, khususnya saat membaca atau menyimpan data ke file Excel.
   - Dapat dipasang menggunakan perintah:  
     ```bash
     pip install pandas
     ```

3. **`openpyxl`**
   - Berfungsi sebagai engine untuk membaca dan menulis file Excel dengan format `.xlsx`.
   - Dapat dipasang menggunakan perintah:  
     ```bash
     pip install openpyxl
     ```

4. **`tkcalendar`**
   - Menyediakan widget kalender untuk memilih tanggal pada antarmuka aplikasi.
   - Dapat dipasang menggunakan perintah:  
     ```bash
     pip install tkcalendar
     ```
### **Pendukung Lainnya**
- File `database_module.py` harus tersedia dalam direktori yang sama dengan program pengguna. Modul ini harus mencakup fungsi seperti `save_data_to_excel` dan variabel `DATABASE_FILE` untuk menyimpan data Excel.

- File gambar yang dirujuk dalam kode (`1.png`, `2.png`, `3.png`, `4.png`, `5.png`) juga perlu tersedia di direktori proyek atau sesuai jalur yang diatur dalam kode.

Setelah semua library terinstal dan file pendukung disiapkan, program dapat dijalankan dengan lancar.
