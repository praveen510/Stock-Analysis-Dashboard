# import yfinance as yf

# ticker = "AMZN"

# # Define start and end dates
# start_date = "2024-03-20"
# end_date = "2025-03-20"

# # Download data
# df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# # Save to CSV
# df.to_csv("AMZN_stock_data.csv")

# print(df.head())


import pandas as pd

# Yahoo Finance CSV download URL
url = "https://query1.finance.yahoo.com/v7/finance/download/AMZN?period1=1709683200&period2=1742485000&interval=1d&events=history&includeAdjustedClose=true"

# Read data from URL into a DataFrame
df = pd.read_csv(url)

# Display the first few rows as a table
print(df.head())

# Save to CSV
df.to_csv("AMZN_stock_data.csv", index=False)


