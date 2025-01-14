import requests

def download_csv(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"CSV data saved to {filename}")
    else:
        print("Failed to retrieve the file. Status code:", response.status_code)
  