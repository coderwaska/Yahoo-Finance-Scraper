# Yahoo Finance Scrape

A Python application that downloads historical cryptocurrency price data from Yahoo Finance. While originally designed for downloading Solana (SOL) cryptocurrency data, it can be used for any cryptocurrency or financial instrument available on Yahoo Finance.

## Description

This tool fetches historical price data at different time intervals (5 days, 3 months, 6 months, 1 year, 5 years, or max available) and saves it in CSV format for further analysis. It uses the `yfinance` library to reliably retrieve data with automatic retries in case of connection issues.

## Features

- Download historical price data for any cryptocurrency/ticker available on Yahoo Finance
- Support for multiple time periods (5d, 3mo, 6mo, 1y, 5y, max)
- Custom date range support
- Automatic retry in case of download failures
- Organized output in CSV format for easy analysis

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/coderwaska/Yahoo-Finance-Scraper.git
   cd Yahoo-Finance-Scraper
   ```

2. Install the required Python packages:
   ```
   pip install yfinance pandas
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Follow the prompts to enter:
   - Currency ticker (e.g., SOL-USD, BTC-USD, ETH-USD)
   - Filename prefix for the output files
   - Optional start date in YYYY-MM-DD format
   - Optional end date in YYYY-MM-DD format (defaults to current date if left empty)

3. The script will download data for various time periods and save CSV files in the `exported_data` folder.

### Example

```
Input Currency (Ex: SOL-USD): SOL-USD
Input Filename Prefix (Ex: solana_usd_historical_data): solana_usd_historical_data
Start Date (YYYY-MM-DD) [optional]: 2021-01-01
End Date (YYYY-MM-DD) [optional]: 
```

This will generate the following output files in the `exported_data` directory:
- `solana_usd_historical_data_5d.csv` - Last 5 days of data
- `solana_usd_historical_data_3_months.csv` - Last 3 months of data
- `solana_usd_historical_data_6_months.csv` - Last 6 months of data
- `solana_usd_historical_data_1_year.csv` - Last 1 year of data
- `solana_usd_historical_data_5_years.csv` - Last 5 years of data
- `solana_usd_historical_data_max.csv` - Maximum available historical data
- `solana_usd_historical_data_daily.csv` - Data from the specified start date to end date

## Data Format

The CSV output files contain the following columns:
- Date
- Open price
- High price
- Low price
- Close price
- Volume

## Advanced Usage

### Using the reliable_download function directly

For more customized data downloads, you can import and use the `reliable_download` function in your own scripts:

```python
from main import reliable_download

# Download 1-week data with 1-hour intervals
reliable_download("SOL-USD", "my_hourly_data.csv", period="1wk", interval="1h")

# Download specific date range with 15-minute intervals
reliable_download("BTC-USD", "bitcoin_custom_range.csv", 
                 start="2023-01-01", end="2023-01-31", 
                 interval="15m")
```

## Troubleshooting

- **Empty data**: Some tickers may not have data for all requested periods. In these cases, the script will show a warning.
- **Connection errors**: The script automatically retries downloads if a connection issue occurs.
- **Invalid ticker**: Make sure the ticker symbol is correct and available on Yahoo Finance.

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

This tool uses the [yfinance](https://pypi.org/project/yfinance/) library to access Yahoo Finance data.
