import requests
import pandas as pd
from datetime import datetime
import os
import re
from fake_useragent import UserAgent

def fetch_data():
    BASE_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata/"
    START_DATE = '2020-09-19'
    END_DATE = datetime.now().strftime('%Y-%m-%d')
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    r = requests.get(BASE_URL + START_DATE, headers=headers)
    data = r.json()

    fng_data = pd.read_csv('fear-greed.csv', usecols=['Date', 'Fear Greed'])
    fng_data['Date'] = pd.to_datetime(fng_data['Date'], format='%Y-%m-%d')  
    fng_data.set_index('Date', inplace=True)

    missing_dates = []
    all_dates = pd.date_range(fng_data.index[0], END_DATE, freq='D')
    for date in all_dates:
        if date not in fng_data.index:
            missing_dates.append(date)
            fng_data.loc[date] = [0]
    fng_data.sort_index(inplace=True)

    for item in data['fear_and_greed_historical']['data']:
        x = datetime.fromtimestamp(item['x'] / 1000).strftime('%Y-%m-%d')
        y = item['y']
        fng_data.at[x, 'Fear Greed'] = y

    # fng_data.to_csv('all_fng_csv4.csv') # no need to save, just use the dataframe
    return fng_data

def format_array(fng_data):
    # From row 3286 up to end
    b_column_values = fng_data.iloc[3286:, 0].values # It's a single column now (Fear Greed)
    b_column_values = [round(value, 2) for value in b_column_values if value != 0]
    
    formatted_lines = []
    for i in range(0, len(b_column_values), 20):
        line = ','.join(map(str, b_column_values[i:i+20])) + ','
        formatted_lines.append('  ' + line)
    
    full_array_str = '\n'.join(formatted_lines)
    if full_array_str.endswith(','):
        full_array_str = full_array_str[:-1]
    return full_array_str

def update_pine(new_array_str):
    pine_file = '../../CNN.pine'
    with open(pine_file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_array_block = "float[] arr = array.from(\n" + new_array_str + ")"
    pattern = re.compile(r'float\[\] arr = array\.from\((.*?)\)', re.DOTALL)
    
    new_content = pattern.sub(new_array_block.replace('\\', '\\\\'), content)

    with open(pine_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    print("Fetching data from CNN...")
    df = fetch_data()
    print("Formatting array...")
    array_str = format_array(df)
    print("Updating CNN.pine...")
    update_pine(array_str)
    print("CNN.pine updated successfully.")

if __name__ == "__main__":
    main()
