#Sample Table to Check Python is working or not
import pandas as pd
data=[['Raj',89],['Rohan',78],['Praveen',56],['Rajesh',56]]
df=pd.DataFrame(data,columns=['Name','Marsks'])
#print(df)

#Step-1: Convert 'YYYY-MM-DD' to UNIX timestamp
import time
def date_to_unix(date_str):
    return int(time.mktime(time.strptime(date_str,"%Y-%m-%d")))

#Example
start_date='2024-03-12'
unix_start_date=date_to_unix(start_date)
#print(f'Start Date: {start_date}, Unix Date: {date_to_unix(start_date)}')

#Step-2: Get the current date in 'YYYY-MM-DD' format
from datetime import datetime
current_date=datetime.now().strftime('%Y-%m-%d')
unix_current_date=date_to_unix(current_date)
#print(f"Current Date: {current_date}, Unix Current Date: {unix_current_date}")

#Step-3: import pandas as pd
file_path="C:\\Users\\Parveen\\Desktop\\Power BI Project 2025\\trackers.csv"
sample_df=pd.read_csv(file_path)
trackers=sample_df['Symbol'].to_list()
#print(f"Stock Symbols")
#print(trackers)

#Step-4: Initialize a list to hold all data
data_frames=[]

#Step-5: Fetch Data from Yahoo Finance 
import yfinance as yf
ticker = "AMZN"
# Define start and end dates
end_date = current_date

# Download data
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")
data_frames.append(df)
combined_data=pd.concat(data_frames,ignore_index=True)
print(combined_data)