import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import numpy as np

# Cek isi folder
folder = "exported_data"
files = [f for f in os.listdir(folder) if f.endswith(".csv")]

if not files:
    print("⚠️ Tidak ada file CSV di folder 'exported_data'.")
    exit()

# Pilihan file
print("Pilih data yang ingin diprediksi (Ex: 1):\n")
for i, f in enumerate(files, 1):
    print(f"{i}. {f}")

try:
    pilihan = int(input("\nMasukkan nomor file: "))
    selected_file = files[pilihan - 1]
except (ValueError, IndexError):
    print("❌ Pilihan tidak valid.")
    exit()

file_path = os.path.join(folder, selected_file)

# Info dari nama file
file_name = selected_file.replace(".csv", "")
parts = file_name.split("_")
asset = parts[0].upper()
currency = parts[1].upper()
raw_time = parts[-2] + "_" + parts[-1] if len(parts) >= 6 else parts[-1]

timeframe_dict = {
    "5d": "5 hari",
    "3_months": "3 bulan",
    "6_months": "6 bulan",
    "1_year": "1 tahun",
    "5_years": "5 tahun",
    "max": "maksimal",
    "daily": "rentang khusus",
    "weekly": "mingguan",
    "monthly": "bulanan"
}
timeframe = timeframe_dict.get(raw_time, raw_time.replace("_", " "))

# Baca CSV
try:
    df = pd.read_csv(file_path, skiprows=[1, 2])
    df.rename(columns={"Price": "Date"}, inplace=True)
except Exception as e:
    print(f"❌ Gagal membaca file: {e}")
    exit()

if 'Date' not in df.columns or 'Close' not in df.columns:
    print("❌ File tidak mengandung kolom 'Date' dan 'Close'.")
    exit()

# Persiapan data
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').drop_duplicates(subset='Date')

print(f"\n📅 Data dari {df['Date'].dt.strftime('%Y-%m-%d').iloc[0]} sampai {df['Date'].dt.strftime('%Y-%m-%d').iloc[-1]}")
print(f"📊 Total data: {len(df)} baris")

# Hitung Moving Average
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# Input tanggal target
target_input = input("\n🕐 Input waktu yang ingin diprediksi harganya (YYYY-MM-DD): ").strip()
try:
    target_date = pd.to_datetime(target_input)
except:
    print("❌ Format tanggal tidak valid.")
    exit()

df_until_target = df[df['Date'] <= target_date]

if df_until_target.empty:
    print("⚠️ Tidak ada data sebelum tanggal tersebut.")
    exit()

# Input jumlah hari terakhir
try:
    range_hari = int(input("📅 Ingin gunakan berapa hari terakhir untuk prediksi? (contoh: 5): ").strip())
    df_recent = df_until_target.tail(range_hari)

    # Konversi ke model prediksi
    df_recent = df_recent.copy()
    df_recent['Days'] = np.arange(len(df_recent)).reshape(-1, 1)

    model = LinearRegression()
    model.fit(df_recent[['Days']], df_recent['Close'])

    next_day = np.array([[len(df_recent)]])
    prediksi = model.predict(next_day)[0]
except:
    prediksi = df_until_target['Close'].mean()
    print("⚠️ Input tidak valid, menggunakan rata-rata seluruh data.")

# Ambil nilai MA terakhir
ma_row = df_until_target.iloc[-1]

# Output hasil prediksi
print(f"\n📈 Prediksi harga {asset} ke {currency} berdasarkan data hingga {target_date.strftime('%Y-%m-%d')} ({timeframe}): ${prediksi:.2f} USD")

print("\n📊 Informasi Moving Average:")
print(f"MA20  : {ma_row['MA20']:.2f}")
print(f"MA50  : {ma_row['MA50']:.2f}")
print(f"MA200 : {ma_row['MA200']:.2f}")

print("\n📌 Sinyal MA Cross:")
print("- MA20 di atas MA50 → kemungkinan uptrend 🟢" if ma_row['MA20'] > ma_row['MA50'] else "- MA20 di bawah MA50 → kemungkinan downtrend 🔴")
print("- MA20 di atas MA200 → jangka panjang cenderung naik 🟢" if ma_row['MA20'] > ma_row['MA200'] else "- MA20 di bawah MA200 → jangka panjang cenderung turun 🔴")
