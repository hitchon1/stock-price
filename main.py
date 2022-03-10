import requests
from datetime import datetime
import time

ticker = input('Enter ticker:')
startDate = input('Enter start: yyyy/mm/dd format:')
endDate = input('Enter start: yyyy/mm/dd format:')

start_datetime = datetime.strptime(startDate,'%Y/%m/%d')
end_datetime = datetime.strptime(endDate,'%Y/%m/%d')

from_epoch = int(time.mktime(start_datetime.timetuple()))
to_epoch = int(time.mktime(end_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url,headers=headers).content
print(content)

with open('data.csv','wb') as file:
  file.write(content)