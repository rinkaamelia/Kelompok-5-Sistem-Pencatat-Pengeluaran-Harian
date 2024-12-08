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
### **1. Library Standar Python**
- **`tkinter`**
  - Sudah termasuk dalam instalasi Python secara default.
  - Pastikan Python diinstal dengan GUI/Tkinter (biasanya otomatis untuk Windows dan macOS).

### **2. Library Eksternal**
- **`Pillow`**
  - Untuk menangani gambar (dalam program ini digunakan untuk memuat gambar background).
  - **Cara instalasi**:
    ```bash
    pip install pillow
    ```

- **`pandas`**
  - Untuk memanipulasi dan membaca/menulis data Excel.
  - **Cara instalasi**:
    ```bash
    pip install pandas
    ```

- **`openpyxl`**
  - Diperlukan oleh pandas untuk membaca/menulis file Excel dalam format `.xlsx`.
  - **Cara instalasi**:
    ```bash
    pip install openpyxl
    ```

- **`tkcalendar`**
  - Untuk menambahkan widget kalender.
  - **Cara instalasi**:
    ```bash
    pip install tkcalendar
    ```

### **3. Modul `database_module`**
- **Custom Module**: Modul ini buatan sendiri, jadi file `database_module.py` harus ada di folder yang sama dengan script ini, atau path-nya harus ditambahkan ke Python.
- Jika tidak ada, Anda harus membuat modul tersebut. Berikut kemungkinan isi dasar untuk modul ini:
  ```python
  import pandas as pd

  DATABASE_FILE = "data.xlsx"  # Nama file database

  def save_data_to_excel(data):
      try:
          # Membaca data jika file sudah ada
          df = pd.read_excel(DATABASE_FILE)
      except FileNotFoundError:
          # Jika file belum ada, buat DataFrame kosong
          df = pd.DataFrame(columns=["tanggal", "jumlah_pemasukan", "jumlah_pengeluaran", "keterangan", "anggaran_mingguan", "sisa_anggaran"])

      # Menambahkan data baru
      df = df.append(data, ignore_index=True)
      # Menyimpan ke file Excel
      df.to_excel(DATABASE_FILE, index=False)
  ```

### **4. Tambahan**
1. **File Gambar**:
   Pastikan file gambar `1.png`, `2.png`, `3.png`, `4.png`, dan `5.png` ada di direktori yang sama dengan script atau sesuai path yang diberikan.
   
2. **Modul `database_module`**:
   Pastikan file `database_module.py` ada di direktori yang sama.

Setelah library diinstal dan file pendukung tersedia, program Anda seharusnya dapat dijalankan tanpa masalah.


   
