import os
import re
from typing import List, Optional

import pandas as pd
import requests
from unidecode import unidecode


CSV_COLUMNS_MAP = {
    "Ngày": "created_at",
    "Tham chiếu": "reference",
    "+/-": "transaction_type",
    "Số tiền": "amount",
    "Nội dung giao dịch": "content",
}


def _slugify_title(title: str) -> str:
    """Make a filesystem-safe, predictable slug from a statement title."""
    safe_title = unidecode(title)
    safe_title = "".join(c for c in safe_title if c.isalnum() or c in (" ", "_", "-", "/")).rstrip()
    safe_title = safe_title.replace(" ", "-").replace("/", "-")
    # Normalize titles that contain dangling day-month-year fragments
    safe_title = re.sub(r"-(\d{1,2})(\d{4})(?=-|$)", r"-\1-\2", safe_title)
    return safe_title.lower()


def download_file(title: str, link: str, download_dir: str) -> Optional[str]:
    """
    Download a CSV and save it under the provided directory.
    Returns the absolute path if successful, otherwise None.
    """
    try:
        filename_slug = _slugify_title(title)
        year_match = re.search(r"-(\d{4})(?=-|\.|$)", filename_slug)
        filename = f"{year_match.group(1)}-{filename_slug}.csv" if year_match else f"{filename_slug}.csv"
        file_path = os.path.join(download_dir, filename)

        if os.path.exists(file_path):
            print(f"File already exists: {file_path}. Skipping download.")
            return file_path

        print(f"Attempting to download '{title}'...")
        response = requests.get(link, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Successfully downloaded and saved to: {file_path}")
        return file_path

    except requests.exceptions.RequestException as err:
        print(f"Error downloading '{title}': {err}")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{title}': {e}")

    return None