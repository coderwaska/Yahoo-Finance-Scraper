import yfinance as yf
import time
from datetime import datetime
import os

def reliable_download(ticker, file_name, max_retries=5, wait_seconds=3, **kwargs):
    retries = 0
    while retries < max_retries:
        try:
            print(f"[{ticker}] Percobaan ke-{retries + 1} - {file_name}")
            data = yf.download(ticker, **kwargs)
            if not data.empty:
                data.to_csv(file_name)
                print(f"✅ Data {ticker} berhasil disimpan ke '{file_name}'\n")
                return True
            else:
                print(f"⚠️ Data {ticker} kosong, coba lagi...")
        except Exception as e:
            print(f"❌ Gagal mengunduh {ticker}: {e}")
        retries += 1
        time.sleep(wait_seconds)
    print(f"❌ Gagal mengambil data {ticker} setelah {max_retries} kali coba.\n")
    return False

# Buat folder 'exported_data' kalau belum ada
output_dir = "exported_data"
os.makedirs(output_dir, exist_ok=True)

# User Input
ticker = input("Input Currency (Ex: BTC-USD): ").strip()

# Auto-generate filename prefix
filename_prefix = ticker.lower().replace("-", "_") + "_historical_data"

# Tanggal
start_date = input("Start Date (YYYY-MM-DD) [optional]: ").strip()
end_date = input("End Date (YYYY-MM-DD) [optional]: ").strip()
if not end_date:
    end_date = datetime.today().strftime('%Y-%m-%d')

# Export data by period
periods = {
    "5d": "5d",
    "3mo": "3_months",
    "6mo": "6_months",
    "1y": "1_year",
    "5y": "5_years",
    "max": "max"
}

for p, label in periods.items():
    file_path = os.path.join(output_dir, f"{filename_prefix}_{label}.csv")
    reliable_download(ticker, file_path, period=p, interval='1d')

# Export data by date
if start_date:
    file_path = os.path.join(output_dir, f"{filename_prefix}_daily.csv")
    reliable_download(ticker, file_path, start=start_date, end=end_date, interval='1d')
else:
    print("⏩ Lewatkan ekspor custom tanggal karena 'start_date' tidak diisi.")

print("Finished")
