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
    image = Image.open("1.png")  # Ganti dengan path gambar Anda
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
    image = Image.open("3.png")  # Ganti dengan path gambar Anda
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

    tk.Label(root, text="Keterangan", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=475, width=500, height=50)
    keterangan_entry = ttk.Combobox(root, font=("Poppins", 30), values=["Uang Bulanan", "Gaji", "Bonus", "Lainnya"], style="TCombobox")
    keterangan_entry.place(x=731, y=525, width=500, height=50)

    def submit_alokasi():
        tanggal = tanggal_entry.get()
        jumlah = jumlah_entry.get()
        keterangan = keterangan_entry.get()

        if not tanggal or not jumlah or not keterangan:
            messagebox.showwarning("Peringatan", "Data tidak lengkap!")
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showwarning("Peringatan", "Jumlah harus berupa angka!")
            return

        anggaran_mingguan = jumlah // 4
        save_data_to_excel({
            "tanggal": tanggal,
            "jumlah_pemasukan": jumlah,
            "jumlah_pengeluaran": 0,
            "keterangan": keterangan,
            "anggaran_mingguan": anggaran_mingguan,
            "sisa_anggaran": anggaran_mingguan
        })
        messagebox.showinfo("Anggaran", f"Anggaran per minggu: {anggaran_mingguan}")
        main_menu()

    tk.Button(root, text="Simpan", font=("Poppins", 24), command=submit_alokasi,  bg= "#68a6e2", fg="white").place(x=910, y=725, width=150, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu),  bg= "#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)

# Fungsi untuk menu pengeluaran
def pengeluaran_menu():
    hide_all()
    # Load gambar background
    image = Image.open("4.png")  # Ganti dengan path gambar Anda
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)
    
    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar
    
    # Style untuk Combobox
    style = ttk.Style()
    style.configure("TCombobox", font=("Poppins", 30))  # Mengatur ukuran font
    
    tk.Label(root, text="Pilih Tanggal", font=("Poppins",30), bg= "#68a6e2", fg="white").place(x=731, y=215, width=500, height=50)
    tanggal_entry = DateEntry(root, date_pattern='yyyy-MM-dd', font=("Poppins", 30), bg= "#acd6fc")
    tanggal_entry.place(x=731, y=265, width=500, height=50)


    tk.Label(root, text="Jumlah Pengeluaran", font=("Poppins",30), bg= "#68a6e2", fg="white").place(x=731, y=345, width=500, height=50)
    jumlah_entry = tk.Entry(root, font=("Poppins", 30), bg= "#acd6fc")
    jumlah_entry.place(x=731, y=395, width=500, height=50)

    tk.Label(root, text="Keterangan", font=("Poppins", 30), bg="#68a6e2", fg="white").place(x=731, y=475, width=500, height=50)
    keterangan_entry = ttk.Combobox(root, font=("Poppins", 30), values=["Makanan", "Transportasi", "Gaya Hidup", "Lainnya"], style="TCombobox")
    keterangan_entry.place(x=731, y=525, width=500, height=50)

    def submit_pengeluaran():
        tanggal = tanggal_entry.get()
        jumlah = jumlah_entry.get()
        keterangan = keterangan_entry.get()

        if not tanggal or not jumlah or not keterangan:
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
            "keterangan": keterangan,
            "anggaran_mingguan": anggaran_mingguan,
            "sisa_anggaran": sisa_anggaran
        })
        messagebox.showinfo("Notifikasi", f"Sisa anggaran saat ini: {sisa_anggaran}")
        main_menu()

    tk.Button(root, text="Simpan", font=("Poppins", 24), command=submit_pengeluaran,  bg= "#68a6e2", fg="white").place(x=910, y=725, width=150, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu),  bg= "#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)


# Fungsi untuk menu laporan bulanan
def laporan_menu():
    hide_all()
    # Load gambar background
    image = Image.open("5.png")  # Ganti dengan path gambar Anda
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(image)
    
    # Tambahkan label untuk menampilkan gambar background
    background_label = tk.Label(root, image=bg_image)
    background_label.image = bg_image  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
    background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh layar
    
    # Label untuk laporan
    laporan_label = tk.Label(root, text="", font=("Poppins", 12), justify="left", anchor="w")
    laporan_label.pack(pady=20)

    tk.Label(root, text="Pilih Tanggal",font=("Poppins",30), bg= "#68a6e2", fg="white").place(x=731, y=215, width=500, height=50)
    laporan_calendar = DateEntry(root, date_pattern='yyyy-MM-dd', font=("Poppins", 30), bg= "#acd6fc")
    laporan_calendar.place(x=731, y=265, width=500, height=50)
    
    def generate_monthly_report():
        df = pd.read_excel(DATABASE_FILE)
        if df.empty:
            laporan_label.config(text="Tidak ada data untuk ditampilkan.")
            return

        # Menghilangkan jam pada kolom "tanggal"
        df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce").dt.date

        # Mendapatkan tanggal yang dipilih dari kalender dan memastikan hanya tanggal (tanpa jam)
        tanggal = laporan_calendar.get()
        tanggal = pd.to_datetime(tanggal).date()

        # Memfilter berdasarkan tanggal yang dipilih
        df_filtered = df[df["tanggal"] == tanggal]

        if df_filtered.empty:
            laporan_label.config(text="Tidak ada data untuk tanggal yang dimasukkan.")
            return

        # Membuat tampilan tabel
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=500, pady=370)

        tree = ttk.Treeview(frame, columns=("Tanggal", "Pemasukan", "Pengeluaran", "Kategori", "Sisa Anggaran"), show="headings")
        tree.heading("Tanggal", text="Tanggal")
        tree.heading("Pemasukan", text="Pemasukan")
        tree.heading("Pengeluaran", text="Pengeluaran")
        tree.heading("Kategori", text="Kategori")
        tree.heading("Sisa Anggaran", text="Sisa Anggaran")

        tree.column("Tanggal", anchor="center", width=150)
        tree.column("Pemasukan", anchor="center", width=150)
        tree.column("Pengeluaran", anchor="center", width=150)
        tree.column("Kategori", anchor="center", width=200)
        tree.column("Sisa Anggaran", anchor="center", width=150)

        tree.pack(fill=tk.BOTH, expand=True)

        # Menampilkan data ke tabel
        total_pemasukan = 0
        total_pengeluaran = 0
        for _, row in df_filtered.iterrows():
            sisa_anggaran = row["jumlah_pemasukan"] - row["jumlah_pengeluaran"]
            total_pemasukan += row["jumlah_pemasukan"]
            total_pengeluaran += row["jumlah_pengeluaran"]

            tree.insert("", tk.END, values=(
                row["tanggal"],
                row["jumlah_pemasukan"],
                row["jumlah_pengeluaran"],
                row["keterangan"],  # Keterangan ditampilkan sebagai Kategori
                sisa_anggaran,
            ))

        # Menambahkan total di bawah tabel
        tree.insert("", tk.END, values=("Total", total_pemasukan, total_pengeluaran, "", total_pemasukan - total_pengeluaran))
        
    tk.Button(root, text="Generate Laporan", font=("Poppins", 24), command=generate_monthly_report,  bg= "#68a6e2", fg="white").place(x=845, y=725, width=280, height=50)
    tk.Button(root, text="Kembali", font=("Poppins", 24), command=lambda: kembali(main_menu),  bg= "#68a6e2", fg="white").place(x=910, y=810, width=150, height=50)

# GUI utama
root = tk.Tk()
root.title("Sistem Pengeluaran")
root.attributes('-fullscreen', True)
root.bind("<Escape>", exit_fullscreen)  # Keluar dari fullscreen dengan tombol Esc

start_screen()
root.mainloop()
