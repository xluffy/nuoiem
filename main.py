import os
import time

import pandas as pd

from utils import download_file

CSV_FILE = "nuoiem.csv"
DOWNLOAD_DIR = "SAOKE/goc"

def main():
    if not os.path.exists(CSV_FILE):
        print(f"Error: CSV file not found at '{CSV_FILE}'.")
        print("Please ensure the list of links is saved in a file named 'bank_statements.csv' in the current directory.")
        return

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        print(f"Created download directory: {DOWNLOAD_DIR}")
    
    df = pd.read_csv(CSV_FILE)
    
    if df.empty:
        print("The CSV file is empty or missing data.")
        return

    successful_downloads = 0
    
    for index, row in df.iterrows():
        title = row['Title'].strip()
        link = row['URL'].strip()

        file_path = download_file(title, link, DOWNLOAD_DIR)
        time.sleep(1)

    print("-" * 50)
    print(f"Download complete! Successful downloads: {successful_downloads}/{len(df)}")
    print(f"Files saved in the '{DOWNLOAD_DIR}' directory.")

if __name__ == "__main__":
    main()
