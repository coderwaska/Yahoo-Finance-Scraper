# Yahoo Finance Scrape

Aplikasi Python yang mengunduh data historis harga cryptocurrency dari Yahoo Finance dan menyediakan prediksi sederhana berdasarkan data tersebut. Aplikasi ini dapat digunakan untuk cryptocurrency atau instrumen keuangan lain yang tersedia di Yahoo Finance.

## Deskripsi

Alat ini mengambil data harga historis pada berbagai interval waktu (5 hari, 3 bulan, 6 bulan, 1 tahun, 5 tahun, atau maksimal data yang tersedia) dan menyimpannya dalam format CSV untuk analisis lebih lanjut. Aplikasi ini menggunakan library `yfinance` untuk mengambil data dengan metode retry otomatis jika terjadi masalah koneksi. Tersedia juga fitur prediksi sederhana berdasarkan data historis yang telah diunduh.

## Fitur

- Unduh data harga historis untuk semua cryptocurrency/ticker yang tersedia di Yahoo Finance
- Mendukung berbagai periode waktu (5d, 3mo, 6mo, 1y, 5y, max)
- Mendukung rentang tanggal kustom
- Retry otomatis jika terjadi kegagalan unduhan
- Output terorganisir dalam format CSV untuk memudahkan analisis
- Prediksi harga berdasarkan data historis hingga tanggal target
- Perhitungan Moving Average (MA20, MA50, MA200) dan analisis sinyal MA cross

## Instalasi

### Prasyarat

- Python 3.6 atau lebih tinggi
- pip (Penginstal paket Python)

### Langkah-langkah Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/coderwaska/Yahoo-Finance-Scraper.git
   cd Yahoo-Finance-Scraper
   ```

2. Instal paket Python yang diperlukan:
   ```
   pip install -r requirements.txt
   ```
   
   Atau instal langsung:
   ```
   pip install yfinance pandas numpy requests
   ```

## Penggunaan

### Pengunduhan Data

1. Jalankan skrip utama:
   ```
   python main.py
   ```

2. Ikuti petunjuk untuk memasukkan:
   - Ticker mata uang (contoh: SOL-USD, BTC-USD, ETH-USD)
   - Tanggal mulai opsional dalam format YYYY-MM-DD
   - Tanggal akhir opsional dalam format YYYY-MM-DD (default ke tanggal saat ini jika dibiarkan kosong)

3. Skrip akan mengunduh data untuk berbagai periode waktu dan menyimpan file CSV di folder `exported_data`.

### Prediksi Harga

1. Setelah mengunduh data, Anda dapat menjalankan skrip prediksi:
   ```
   python prediksi.py
   ```

2. Pilih file data yang ingin digunakan untuk prediksi dari daftar yang ditampilkan.

3. Masukkan tanggal target yang ingin diprediksi harganya.

4. Skrip akan menampilkan:
   - Prediksi harga berdasarkan rata-rata data hingga tanggal target
   - Nilai Moving Average (MA20, MA50, MA200) pada tanggal tersebut
   - Analisis sinyal MA cross dan indikasi kemungkinan trend pasar

### Contoh Penggunaan

```
Input Currency (Ex: BTC-USD): BTC-USD
Start Date (YYYY-MM-DD) [optional]: 2021-01-01
End Date (YYYY-MM-DD) [optional]: 
```

Ini akan menghasilkan file output berikut di direktori `exported_data`:
- `btc_usd_historical_data_5d.csv` - Data 5 hari terakhir
- `btc_usd_historical_data_3_months.csv` - Data 3 bulan terakhir
- `btc_usd_historical_data_6_months.csv` - Data 6 bulan terakhir
- `btc_usd_historical_data_1_year.csv` - Data 1 tahun terakhir
- `btc_usd_historical_data_5_years.csv` - Data 5 tahun terakhir
- `btc_usd_historical_data_max.csv` - Data historis maksimum yang tersedia
- `btc_usd_historical_data_daily.csv` - Data dari tanggal mulai hingga tanggal akhir yang ditentukan

## Format Data

File CSV output berisi kolom-kolom berikut:
- Tanggal
- Harga pembukaan (Open)
- Harga tertinggi (High)
- Harga terendah (Low)
- Harga penutupan (Close)
- Volume

## Penggunaan Lanjutan

### Menggunakan fungsi reliable_download secara langsung

Untuk unduhan data yang lebih kustom, Anda dapat mengimpor dan menggunakan fungsi `reliable_download` di skrip Anda sendiri:

```python
from main import reliable_download

# Unduh data 1 minggu dengan interval 1 jam
reliable_download("SOL-USD", "my_hourly_data.csv", period="1wk", interval="1h")

# Unduh rentang tanggal tertentu dengan interval 15 menit
reliable_download("BTC-USD", "bitcoin_custom_range.csv", 
                 start="2023-01-01", end="2023-01-31", 
                 interval="15m")
```

### Menggunakan Fitur Prediksi

Skrip `prediksi.py` menyediakan beberapa analisis dan prediksi berdasarkan data historis yang telah diunduh:

1. **Prediksi Harga**: Menghitung rata-rata harga penutupan (Close) untuk semua data hingga tanggal yang ditentukan.
2. **Moving Average**: Menampilkan nilai MA20, MA50, dan MA200 pada tanggal target.
3. **Analisis MA Cross**: Memberikan indikator trend pasar berdasarkan persilangan Moving Average.

Contoh output prediksi:
```
📈 Prediksi harga BTC ke USD berdasarkan data hingga 2023-05-01 (1 tahun): $35267.89 USD

📊 Informasi Moving Average:
MA20  : 29876.54
MA50  : 27345.67
MA200 : 24567.89

📌 Sinyal MA Cross:
- MA20 di atas MA50 → kemungkinan uptrend 🟢
- MA20 di atas MA200 → jangka panjang cenderung naik 🟢
```

## Pemecahan Masalah

- **Data kosong**: Beberapa ticker mungkin tidak memiliki data untuk semua periode yang diminta. Dalam kasus ini, skrip akan menampilkan peringatan.
- **Error koneksi**: Skrip secara otomatis mencoba mengulang unduhan jika terjadi masalah koneksi.
- **Ticker tidak valid**: Pastikan simbol ticker benar dan tersedia di Yahoo Finance.

## Lisensi

Proyek ini bersifat open source dan tersedia di bawah [Lisensi MIT](LICENSE).

## Kredit

Alat ini menggunakan library [yfinance](https://pypi.org/project/yfinance/) untuk mengakses data Yahoo Finance.