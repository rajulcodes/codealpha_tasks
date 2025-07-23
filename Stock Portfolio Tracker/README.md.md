# Stock Portfolio Tracker 📊

An enhanced Python script to manage and analyze stock investments with improved features and file export options.

## Features
- Input stock symbols and quantities with validation
- Hardcoded dictionary of stock prices
- Calculates individual and total investment value
- Supports re-entry of the same stock (accumulates quantity)
- Saves report in `.txt` or `.csv` format

## Technologies Used
- Python 3
- Concepts: dictionaries, loops, functions, exception handling, user input, file operations

## How to Run

1. Make sure you have Python 3 installed
2. Save the script as `stock_portfolio_tracker.py`
3. Run the script:

```bash
python stock_portfolio_tracker.py
```

## Sample Workflow
```
Welcome to the Simple Stock Portfolio Tracker! 📈
--- Available Stock Prices ---
AAPL: $180.00
MSFT: $420.50
...
Enter stock symbol (e.g., AAPL) or 'done': AAPL
Enter quantity for AAPL: 5
Added 5 shares of AAPL worth $900.00
...
Total Investment Value: $2450.75
Do you want to save the portfolio report? (yes/no): yes
Save as (txt/csv)? csv
Portfolio saved to stock_portfolio_csv.csv
```

## Available Stocks (can be modified)
```python
{
    "AAPL": 180.00,
    "MSFT": 420.50,
    "GOOG": 175.25,
    "AMZN": 190.75,
    "TSLA": 250.00,
    "NVDA": 1200.00,
    "META": 495.00
}
```

## File Output Format
### Text Format
- Human-readable portfolio summary in plain text

### CSV Format
- Table format with columns: Symbol, Quantity, Price Per Share, Holding Value

## License
This project is MIT licensed.

---
Track smart, invest smarter! 📉
