import requests
import os
from datetime import datetime, timedelta

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Successfully downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

base_url = "https://s3.amazonaws.com/tripdata/"

files = []

for year in range(2013, 2024):
    files.append(f"{year}-citibike-tripdata.zip")

# Monthly data for 2024 up to May
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 5, 1)
current_date = start_date

while current_date <= end_date:
    files.append(f"{current_date.strftime('%Y%m')}-citibike-tripdata.csv.zip")
    current_date += timedelta(days=32)
    current_date = current_date.replace(day=1)

if not os.path.exists("citibike_data"):
    os.makedirs("citibike_data")

for file in files:
    url = base_url + file
    filename = os.path.join("citibike_data", file)
    download_file(url, filename)

print("All files have been downloaded.")
