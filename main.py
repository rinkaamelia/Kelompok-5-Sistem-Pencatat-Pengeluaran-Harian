import tkinter as tk
from main_menu import start_screen, main_menu

def main_menu(root):
     for widget in root.winfo_children():
        widget.destroy()
    
if __name__ == "__main__":
    # Buat instance root
    root = tk.Tk()
    root.title("Meowallet")
    root.geometry("1920x1080")  # Set ukuran jendela
    root.attributes('-fullscreen', True)  # Mode fullscreen

    # Tampilkan layar awal
    start_screen(root, main_menu)

    # Jalankan event loop Tkinter
    root.mainloop()
