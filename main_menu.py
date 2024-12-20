import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL untuk gambar transparan
import pandas as pd
from tkcalendar import DateEntry
from database_module import DATABASE_FILE, save_data_to_excel

# Fungsi untuk menyembunyikan semua elemen
def hide_all():
    for widget in root.winfo_children():
        widget.pack_forget()
        
# Fungsi untuk menu utama
def main_menu():
    hide_all()

# Fungsi untuk kembali ke menu sebelumnya
def kembali(menu):
    menu()

# Fungsi untuk keluar dari fullscreen
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Fungsi untuk tampilan awal dengan background gambar
def start_screen():
    hide_all()  
    # Load gambar background
    image = Image.open("1.png")  
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)
    
    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar
    
    # Tambahkan elemen di atas background
    tk.Label(root, text="Meowallet", font=("Starborn", 125), fg="#acd6fc", bg="#f8fbff").place(x=313, y=403)
    tk.Button(root, text="Mulai", font=("Poppins", 24), command=main_menu, bg="#68a6e2", fg="#f8fbff").place(x=891, y=665)
    tk.Button(root, text="Keluar", font=("Poppins", 24), command=root.quit, bg="#68a6e2", fg="#f8fbff").place(x=885 ,y=800)

# Fungsi untuk menu utama
def main_menu():
    hide_all()
    # Load gambar background
    image = Image.open("2.png")  # Pastikan path gambar sesuai
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)

    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar

    # Tambahkan elemen menu
    tk.Button(root, text="Alokasi", font=("Poppins", 30), command=alokasi_menu, bg= "#68a6e2", fg="white").place(x=713, y=273, width=494, height=113)
    tk.Button(root, text="Pengeluaran", font=("Poppins", 30), command=pengeluaran_menu, bg="#68a6e2", fg="white").place(x=713, y=441, width=494, height=113)
    tk.Button(root, text="Laporan Bulanan", font=("Poppins", 30), command=laporan_menu, bg="#68a6e2", fg="white").place(x=713, y=609, width=494, height=113)
    tk.Button(root, text="Kembali", font=("Poppins", 30), command=lambda: kembali(start_screen), bg="#68a6e2", fg="white").place(x=713, y=778, width=494, height=113)

# Fungsi untuk menu alokasi
def alokasi_menu():
    hide_all()
    # Load gambar background
    image = Image.open("3.png") 
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)
    
    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar
    
    # Style untuk Combobox
    style = ttk.Style()
    style.configure("TCombobox", font=("Poppins", ))  # Mengatur ukuran font
    
    tk.Label(root, text="Pilih Tanggal", font=("Poppins",30), bg= "#68a6e2", fg="white").place(x=731, y=215, width=500, height=50)
    tanggal_entry = DateEntry(root, date_pattern='yyyy-MM-dd', font=("Poppins", 30))
    tanggal_entry.place(x=731, y=265, width=500, height=50)

    tk.Label(root, text="Jumlah Pemasukan", font=("Poppins",30), bg= "#68a6e2", fg="white").place(x=731, y=345, width=500, height=50)
    jumlah_entry = tk.Entry(root, font=("Poppins", 30))
    jumlah_entry.place(x=731, y=395, width=500, height=50)

    tk.Label(root, text="Kategori", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=475, width=500, height=50)
    kategori_entry = ttk.Combobox(root, font=("Poppins", 30), values=["Uang Bulanan", "Gaji", "Bonus", "Lainnya"], style="TCombobox")
    kategori_entry.place(x=731, y=525, width=500, height=50)

    def submit_alokasi():
        tanggal = tanggal_entry.get()
        jumlah = jumlah_entry.get()
        kategori = kategori_entry.get()

        if not tanggal or not jumlah or not kategori:
            messagebox.showwarning("Peringatan", "Data tidak lengkap!")
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showwarning("Peringatan", "Jumlah harus berupa angka!")
            return

        # Membaca data dari file
        df = pd.read_excel(DATABASE_FILE)
    
        # Mendapatkan total pemasukan yang sudah ada sebelumnya
        total_pemasukan = df["jumlah_pemasukan"].sum() if "jumlah_pemasukan" in df.columns else 0
    
        # Menghitung anggaran mingguan berdasarkan total pemasukan
        anggaran_mingguan = (total_pemasukan + jumlah) // 4  # Total pemasukan + pemasukan baru dibagi 4 minggu
        sisa_anggaran = anggaran_mingguan  # Sisa anggaran adalah anggaran mingguan yang baru

        # Simpan data baru ke Excel
        save_data_to_excel({
            "tanggal": tanggal,
            "jumlah_pemasukan": jumlah,
            "jumlah_pengeluaran": 0,
            "kategori": kategori,
            "anggaran_mingguan": anggaran_mingguan,
            "sisa_anggaran": sisa_anggaran
        })

        messagebox.showinfo("Anggaran", f"Anggaran per minggu: {anggaran_mingguan}")
        main_menu()

    tk.Button(root, text="Simpan", font=("Poppins", 24), command=submit_alokasi,  bg= "#68a6e2", fg="white").place(x=910, y=725, width=150, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu),  bg= "#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)

# Fungsi untuk menu pengeluaran
def pengeluaran_menu():
    hide_all()
    # Load gambar background
    image = Image.open("4.png")  
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)
    
    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar

    # Style untuk Combobox
    style = ttk.Style()
    style.configure("TCombobox", font=("Poppins", 30))  # Mengatur ukuran font

    tk.Label(root, text="Pilih Tanggal", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=215, width=500, height=50)
    tanggal_entry = DateEntry(root, date_pattern='yyyy-MM-dd', font=("Poppins", 30), bg="#acd6fc")
    tanggal_entry.place(x=731, y=265, width=500, height=50)

    tk.Label(root, text="Jumlah Pengeluaran", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=345, width=500, height=50)
    jumlah_entry = tk.Entry(root, font=("Poppins", 30), bg="#acd6fc")
    jumlah_entry.place(x=731, y=395, width=500, height=50)

    tk.Label(root, text="Kategori", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=475, width=500, height=50)
    kategori_entry = ttk.Combobox(root, font=("Poppins", 30), values=["Makanan", "Transportasi", "Gaya Hidup", "Lainnya"], style="TCombobox")
    kategori_entry.place(x=731, y=525, width=500, height=50)

    tk.Label(root, text="Keterangan", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=605, width=500, height=50)
    keterangan_entry = tk.Entry(root, font=("Poppins", 30), bg="#acd6fc")
    keterangan_entry.place(x=731, y=655, width=500, height=50)

    def submit_pengeluaran():
        tanggal = tanggal_entry.get()
        jumlah = jumlah_entry.get()
        kategori = kategori_entry.get()
        keterangan = keterangan_entry.get()

        if not tanggal or not jumlah or not kategori or not keterangan:
            messagebox.showwarning("Peringatan", "Data tidak lengkap!")
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showwarning("Peringatan", "Jumlah harus berupa angka!")
            return

        df = pd.read_excel(DATABASE_FILE)
        total_pemasukan = df["jumlah_pemasukan"].sum() if "jumlah_pemasukan" in df.columns else 0
        total_pengeluaran = df["jumlah_pengeluaran"].sum() if "jumlah_pengeluaran" in df.columns else 0
        anggaran_mingguan = total_pemasukan // 4
        sisa_anggaran = anggaran_mingguan - (total_pengeluaran + jumlah)

        save_data_to_excel({
            "tanggal": tanggal,
            "jumlah_pemasukan": 0,
            "jumlah_pengeluaran": jumlah,
            "kategori": kategori,
            "keterangan": keterangan,
            "anggaran_mingguan": anggaran_mingguan,
            "sisa_anggaran": sisa_anggaran
        })
        messagebox.showinfo("Notifikasi", f"Sisa anggaran saat ini: {sisa_anggaran}")
        main_menu()

    tk.Button(root, text="Simpan", font=("Poppins", 24), command=submit_pengeluaran, bg="#68a6e2", fg="white").place(x=910, y=725, width=150, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu), bg="#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)

# Fungsi untuk menu laporan bulanan
def laporan_menu():
    hide_all()
    # Load gambar background
    image = Image.open("5.png") 
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)

    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar

    # Label untuk laporan
    laporan_label = tk.Label(root, text="", font=("Poppins", 12), justify="left", anchor="w")
    laporan_label.pack(pady=20)

    tk.Label(root, text="Pilih Bulan", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=215, width=500, height=50)
    
    # Dropdown untuk memilih bulan
    bulan_combobox = ttk.Combobox(root, font=("Poppins", 30), values=[
        "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ])
    bulan_combobox.place(x=731, y=265, width=500, height=50)

    def generate_monthly_report():
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        df = pd.read_excel(DATABASE_FILE)
        if df.empty:
            laporan_label.config(text="Tidak ada data untuk ditampilkan.")
            return

        # Pastikan kolom "tanggal" terkonversi dengan benar
        df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
    
        # Verifikasi apakah ada nilai yang tidak bisa dikonversi
        invalid_dates = df[df["tanggal"].isna()]
        if not invalid_dates.empty:
            print("Data tanggal yang tidak valid:")
            print(invalid_dates)

        # Mendapatkan bulan yang dipilih
        selected_month = bulan_combobox.get()
        if not selected_month:
            messagebox.showwarning("Peringatan", "Harap pilih bulan!")
            return

        # Konversi bulan ke angka
        month_map = {
            "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
            "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
        }
        selected_month_num = month_map.get(selected_month)

        # Setel notifikasi ke pesan default (kosong) sebelum pengecekan
        laporan_label.config(text="")  # Ini untuk menghapus pesan sebelumnya
        
        # Filter data berdasarkan bulan
        df_filtered = df[df["tanggal"].dt.month == selected_month_num]

        if df_filtered.empty:
            laporan_label.config(text="Tidak ada data untuk bulan yang dipilih.")
            return

        # Debug: Menampilkan data yang sudah difilter
        print("Data yang difilter untuk bulan:", selected_month)
        print(df_filtered)

        # Membuat tampilan tabel
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=350, pady=400)

        tree = ttk.Treeview(frame, columns=("Tanggal", "Pemasukan", "Pengeluaran", "Kategori", "Keterangan", "Sisa Anggaran"), show="headings")
        tree.heading("Tanggal", text="Tanggal")
        tree.heading("Pemasukan", text="Pemasukan")
        tree.heading("Pengeluaran", text="Pengeluaran")
        tree.heading("Kategori", text="Kategori")
        tree.heading("Keterangan", text="Keterangan")
        tree.heading("Sisa Anggaran", text="Sisa Anggaran")

        tree.column("Tanggal", anchor="center", width=150)
        tree.column("Pemasukan", anchor="center", width=150)
        tree.column("Pengeluaran", anchor="center", width=150)
        tree.column("Kategori", anchor="center", width=150)
        tree.column("Keterangan", anchor="center", width=150)
        tree.column("Sisa Anggaran", anchor="center", width=150)

        tree.pack(fill=tk.BOTH, expand=True)

        # Menampilkan data ke tabel
        total_pemasukan = 0
        total_pengeluaran = 0
        running_balance = 0  # Variabel untuk menghitung anggaran yang tersisa secara kumulatif

        for _, row in df_filtered.iterrows():
            # Update running balance (sisa anggaran) berdasarkan pemasukan dan pengeluaran kumulatif
            running_balance += row["jumlah_pemasukan"] - row["jumlah_pengeluaran"]
    
            # running_balance tidak pernah negatif
            sisa_anggaran = max(running_balance, 0)

            total_pemasukan += row["jumlah_pemasukan"]
            total_pengeluaran += row["jumlah_pengeluaran"]

            # Mengubah nilai "Keterangan" yang kosong menjadi "-"
            kategori = row["kategori"] if pd.notna(row["kategori"]) else "-"
            keterangan = row["keterangan"] if pd.notna(row["keterangan"]) else "-"

            tree.insert("", tk.END, values=(
                row["tanggal"].strftime("%Y-%m-%d"),
                row["jumlah_pemasukan"],
                row["jumlah_pengeluaran"],
                kategori,  # Keterangan dipindah ke kategori
                keterangan,
                sisa_anggaran,  # Sisa anggaran yang dihitung secara kumulatif
            ))

        # Menambahkan total di bawah tabel
        tree.insert("", tk.END, values=("Total", total_pemasukan, total_pengeluaran, "", "", total_pemasukan - total_pengeluaran))

    tk.Button(root, text="Generate Laporan", font=("Poppins", 24), command=generate_monthly_report, bg="#68a6e2", fg="white").place(x=845, y=725, width=280, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu), bg="#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)


# GUI utama
root = tk.Tk()
root.title("Sistem Pengeluaran")
root.attributes('-fullscreen', True)
root.bind("<Escape>", exit_fullscreen)  # Keluar dari fullscreen dengan tombol Esc

start_screen()
root.mainloop()
