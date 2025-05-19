import pandas as pd
import os

# Cek isi folder
folder = "exported_data"
files = [f for f in os.listdir(folder) if f.endswith(".csv")]

if not files:
    print("⚠️ Tidak ada file CSV di folder 'exported_data'.")
    exit()

# Tampilkan pilihan file
print("Pilih data yang ingin diprediksi (Ex: 1):\n")
for i, f in enumerate(files, 1):
    print(f"{i}. {f}")

# Input pilihan
try:
    pilihan = int(input("\nMasukkan nomor file: "))
    selected_file = files[pilihan - 1]
except (ValueError, IndexError):
    print("❌ Pilihan tidak valid.")
    exit()

file_path = os.path.join(folder, selected_file)

# Ambil nama prefix dan timeframe dari nama file
file_name = selected_file.replace(".csv", "")
parts = file_name.split("_")

# Ambil aset dan currency
asset = parts[0].upper()
currency = parts[1].upper()

# Ambil raw_time dari 2 bagian terakhir
if len(parts) >= 6:
    raw_time = parts[-2] + "_" + parts[-1]
else:
    raw_time = parts[-1]

# Konversi timeframe biar enak dibaca :v
timeframe_dict = {
    "5d": "5 hari",
    "3_months": "3 bulan",
    "6_months": "6 bulan",
    "1_year": "1 tahun",
    "5_years": "5 tahun",
    "max": "maksimal",
    "daily": "rentang khusus"
}
timeframe = timeframe_dict.get(raw_time, raw_time.replace("_", " "))

# Baca file CSV
try:
    df = pd.read_csv(file_path, skiprows=[1, 2])
    df.rename(columns={"Price": "Date"}, inplace=True)
except Exception as e:
    print(f"❌ Gagal membaca file: {e}")
    exit()

# Validasi kolom
if 'Date' not in df.columns or 'Close' not in df.columns:
    print("❌ File tidak mengandung kolom 'Date' dan 'Close'.")
    exit()

# Prediksi harga
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
last_5 = df.tail(5)
prediksi = last_5['Close'].mean()

# Output
print(f"\n📈 Prediksi harga {asset} ke {currency} berdasarkan data {timeframe}: ${prediksi:.2f} USD")
