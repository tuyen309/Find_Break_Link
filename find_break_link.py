import csv
import requests

def read_links_from_csv(file_path):
    links = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Ensure the row is not empty
                    links.append(row[0])  # Assuming links are in the first column
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return links

def check_links(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"OK: {url}")
            else:
                print(f"Broken: {url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Broken: {url} (Error: {e})")

# File path to the CSV file
csv_file_path = "list_link.csv"

# Read links from the CSV file
url_list = read_links_from_csv(csv_file_path)

# Check the links
if url_list:
    check_links(url_list)
else:
    print("No links found in the CSV file.")