# Nama file Excel untuk database
import pandas as pd

DATABASE_FILE = "database.xlsx"

# Fungsi untuk menyimpan data ke Excel
def save_data_to_excel(data, filename=DATABASE_FILE):
    try:
        df_existing = pd.read_excel(filename)
    except FileNotFoundError:
        df_existing = pd.DataFrame()
    df_new = pd.DataFrame([data])
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_excel(filename, index=False)
